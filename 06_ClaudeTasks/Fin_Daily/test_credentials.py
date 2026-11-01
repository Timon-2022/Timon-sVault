"""Offline checks for credential handling; no browser or network access."""

import ast
import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent


class CredentialTests(unittest.TestCase):
    def load_config(self, path, environ):
        spec = importlib.util.spec_from_file_location("credentials", ROOT / "credentials.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.load_config(path, environ=environ)

    def test_runtime_credentials_override_legacy_values_without_writing(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"
            original = json.dumps({"rss": {"lingowhale_username": "example-only-user",
                                           "lingowhale_password": "example-only-password",
                                           "require_login": True}})
            path.write_text(original)
            config = self.load_config(path, {"LINGOWHALE_USERNAME": "runtime-user",
                                            "LINGOWHALE_PASSWORD": "runtime-password"})
            self.assertEqual(config["rss"]["lingowhale_username"], "runtime-user")
            self.assertEqual(config["rss"]["lingowhale_password"], "runtime-password")
            self.assertTrue(config["rss"]["require_login"])
            self.assertEqual(path.read_text(), original)

    def test_missing_environment_never_falls_back_to_legacy_password(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"
            path.write_text(json.dumps({"rss": {"lingowhale_password": "example-only-password"}}))
            config = self.load_config(path, {})
            self.assertEqual(config["rss"]["lingowhale_username"], "")
            self.assertEqual(config["rss"]["lingowhale_password"], "")

    def test_empty_configuration_is_supported(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"
            path.write_text("{}")
            self.assertEqual(self.load_config(path, {})["rss"]["lingowhale_password"], "")

    def test_cookie_file_is_private_even_if_it_already_exists(self):
        # Execute only this small function, without importing or launching Playwright.
        tree = ast.parse((ROOT / "login_lingowhale.py").read_text())
        function = next(node for node in ast.walk(tree)
                        if isinstance(node, ast.FunctionDef) and node.name == "save_cookies")
        namespace = {"os": os, "json": json}
        exec(compile(ast.Module(body=[function], type_ignores=[]), "save_cookies", "exec"), namespace)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "cookies.json"
            path.write_text("[]")
            path.chmod(0o644)
            namespace["save_cookies"]([], str(path))
            self.assertEqual(path.stat().st_mode & 0o777, 0o600)


if __name__ == "__main__":
    unittest.main()
