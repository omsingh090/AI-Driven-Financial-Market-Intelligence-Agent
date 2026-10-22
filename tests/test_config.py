import os
import pytest
from unittest.mock import patch
from config.settings import Settings

class TestSettings:
    """Tests for application settings and environment validation"""

    def test_default_values(self):
        assert Settings.USER_AGENT == os.getenv("USER_AGENT", "AI-Driven-Financial-Market-Intelligence-Agent")
        assert Settings.LLM_MODEL == "gemini-2.0-flash"
        assert Settings.MAX_CONCURRENT_AGENTS == 4
        assert Settings.AGENT_TIMEOUT == 300

    def test_validate_missing_required_keys(self):
        with patch.object(Settings, 'GOOGLE_API_KEY', None), \
             patch.object(Settings, 'TAVILY_API_KEY', None):
            with pytest.raises(ValueError, match="Missing required environment variables"):
                Settings.validate()

    def test_validate_success_with_keys(self):
        with patch.object(Settings, 'GOOGLE_API_KEY', 'test-google-key'), \
             patch.object(Settings, 'TAVILY_API_KEY', 'test-tavily-key'):
            assert Settings.validate() is True

    def test_ensure_directories(self, tmp_path):
        test_reports = str(tmp_path / "reports")
        test_assets = str(tmp_path / "assets")
        test_exports = str(tmp_path / "exports")
        
        with patch.object(Settings, 'REPORTS_DIR', test_reports), \
             patch.object(Settings, 'ASSETS_DIR', test_assets), \
             patch.object(Settings, 'EXPORTS_DIR', test_exports):
            Settings.ensure_directories()
            assert os.path.exists(test_reports)
            assert os.path.exists(test_assets)
            assert os.path.exists(test_exports)
