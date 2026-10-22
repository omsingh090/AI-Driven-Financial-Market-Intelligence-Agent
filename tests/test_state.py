import pytest
from core.state import MarketIntelligenceState

class TestMarketIntelligenceState:
    """Tests for state validation and serialization"""

    def test_default_state_initialization(self):
        state = MarketIntelligenceState()
        assert state.market_domain == "EdTech"
        assert state.raw_news_data == []
        assert state.competitor_data == []
        assert state.state_id is not None
        assert len(state.state_id) > 0

    def test_valid_market_domain(self):
        state = MarketIntelligenceState(market_domain="Fintech-AI 2026")
        assert state.market_domain == "Fintech-AI 2026"

    def test_invalid_market_domain(self):
        with pytest.raises(ValueError, match="Market domain must contain only"):
            MarketIntelligenceState(market_domain="Crypto$$$!")

    def test_query_validation(self):
        # Query under 5 characters should fail
        with pytest.raises(ValueError, match="at least 5 characters"):
            MarketIntelligenceState(query="ai")

        # Valid query
        valid = MarketIntelligenceState(query="EdTech market valuation in 2026")
        assert valid.query == "EdTech market valuation in 2026"
