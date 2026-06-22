import pytest

class BaseTest:
    DEFAULT_TOLERANCE = 1.0
    
    def assert_close(
        self,
        actual: float,
        expected: float,
        tolerance: float = None,
        message: str = ""
    ):
        tol = tolerance if tolerance is not None else self.DEFAULT_TOLERANCE
        assert actual == pytest.approx(expected, abs=tol), (
            message or f"Expected ~{expected:.2f}, got {actual:.2f} (±{tol})"
        )