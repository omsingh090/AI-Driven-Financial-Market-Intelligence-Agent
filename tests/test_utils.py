import os
import json
from datetime import datetime
from core.utils import (
    safe_json_loads,
    safe_json_dumps,
    sanitize_filename,
    ensure_dir_exists,
    get_file_size_mb,
    format_timestamp,
    truncate_text,
    extract_key_metrics,
)

class TestUtils:
    """Tests for core utility functions"""

    def test_safe_json_loads_valid(self):
        result = safe_json_loads('{"ticker": "NVDA", "sentiment": 0.85}')
        assert result == {"ticker": "NVDA", "sentiment": 0.85}

    def test_safe_json_loads_invalid(self):
        assert safe_json_loads('invalid json', default={"error": True}) == {"error": True}
        assert safe_json_loads(None, default=[]) == []

    def test_safe_json_dumps(self):
        data = {"ticker": "AAPL", "updated_at": datetime(2026, 1, 1, 12, 0)}
        dumped = safe_json_dumps(data)
        assert "AAPL" in dumped
        assert "2026-01-01" in dumped

    def test_sanitize_filename(self):
        raw = "Market Intelligence: Report #1 (EdTech)!"
        sanitized = sanitize_filename(raw)
        assert "market_intelligence__report__1__edtech__" == sanitized
        assert " " not in sanitized
        assert ":" not in sanitized

    def test_ensure_dir_exists(self, tmp_path):
        target = str(tmp_path / "nested" / "output_dir")
        assert ensure_dir_exists(target) is True
        assert os.path.isdir(target)

    def test_get_file_size_mb(self, tmp_path):
        test_file = tmp_path / "test.txt"
        test_file.write_bytes(b"A" * (1024 * 1024))  # 1 MB
        size = get_file_size_mb(str(test_file))
        assert round(size, 1) == 1.0

    def test_truncate_text(self):
        short = "Financial update"
        assert truncate_text(short, 50) == short

        long_text = "A" * 120
        truncated = truncate_text(long_text, 50)
        assert len(truncated) == 50
        assert truncated.endswith("...")

    def test_extract_key_metrics(self):
        empty_metrics = extract_key_metrics([])
        assert empty_metrics["total"] == 0
        assert "No data" in empty_metrics["summary"]

        sample_data = [{"source": "Bloomberg", "title": "Fed Rates"}]
        metrics = extract_key_metrics(sample_data)
        assert metrics["total"] == 1
        assert metrics["sample"] == sample_data[0]
