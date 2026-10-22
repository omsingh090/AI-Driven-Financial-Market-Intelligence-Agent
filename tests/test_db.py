import os
import pytest
from core.db import DatabaseManager
from core.state import MarketIntelligenceState

@pytest.fixture
def db(tmp_path):
    db_file = str(tmp_path / "test_market_intelligence.db")
    return DatabaseManager(db_path=db_file)

class TestDatabaseManager:
    """Tests for SQLite persistence operations"""

    def test_save_and_load_state(self, db):
        state = MarketIntelligenceState(
            market_domain="Healthcare",
            query="AI in diagnostics growth",
            raw_news_data=[{"headline": "AI startup raises $50M"}]
        )
        db.save_state(state)

        loaded = db.load_state(state.state_id)
        assert loaded is not None
        assert loaded.state_id == state.state_id
        assert loaded.market_domain == "Healthcare"
        assert loaded.query == "AI in diagnostics growth"
        assert len(loaded.raw_news_data) == 1

    def test_get_all_states(self, db):
        state1 = MarketIntelligenceState(market_domain="CleanTech", query="Solar innovation 2026")
        state2 = MarketIntelligenceState(market_domain="BioTech", query="CRISPR therapeutics")
        db.save_state(state1)
        db.save_state(state2)

        states = db.get_all_states()
        assert len(states) == 2
        domains = [s["market_domain"] for s in states]
        assert "CleanTech" in domains
        assert "BioTech" in domains

    def test_chat_history_save_and_load(self, db):
        session_id = "test-session-123"
        db.save_chat_message(session_id, "user", "What is the market size?")
        db.save_chat_message(session_id, "assistant", "The market size is $10B.")

        history = db.load_chat_history(session_id)
        assert len(history) == 2
        assert history[0]["type"] == "user"
        assert history[0]["content"] == "What is the market size?"
        assert history[1]["type"] == "assistant"
