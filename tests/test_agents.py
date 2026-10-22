import asyncio
import pytest
from core.agents.base_agent import BaseAgent, AgentStatus

class DummySuccessAgent(BaseAgent):
    """Test implementation of BaseAgent that succeeds"""
    async def execute(self, input_data):
        self.update_progress(50, "Processing data")
        return {"result": f"processed_{input_data.get('key')}"}

class DummyFailAgent(BaseAgent):
    """Test implementation of BaseAgent that raises an exception"""
    async def execute(self, input_data):
        raise RuntimeError("Simulated failure in agent pipeline")

@pytest.mark.asyncio
class TestBaseAgent:
    """Tests for agent lifecycle, state transitions, and error handling"""

    async def test_agent_initialization(self):
        agent = DummySuccessAgent("TestAgent", "A test agent")
        assert agent.name == "TestAgent"
        assert agent.status == AgentStatus.IDLE
        assert agent.progress == 0

    async def test_agent_successful_run(self):
        agent = DummySuccessAgent("SuccessAgent")
        result = await agent.run({"key": "finance_data"})

        assert agent.status == AgentStatus.COMPLETED
        assert agent.progress == 100
        assert agent.start_time is not None
        assert agent.end_time is not None
        assert result == {"result": "processed_finance_data"}

        status = agent.get_status()
        assert status["name"] == "SuccessAgent"
        assert status["status"] == "completed"
        assert status["progress"] == 100
        assert status["duration"] is not None

    async def test_agent_failure_handling(self):
        agent = DummyFailAgent("FailAgent")
        result = await agent.run({})

        assert agent.status == AgentStatus.FAILED
        assert agent.error_message == "Simulated failure in agent pipeline"
        assert result["success"] is False
        assert "Simulated failure" in result["error"]
