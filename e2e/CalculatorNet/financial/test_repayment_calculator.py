import pytest
from playwright.sync_api import expect
from common.base.base_test import BaseTest
from common.utils.data_loader import load_test_data

_DATA = load_test_data("CalculatorNet","financial", "repayment_calculator_data.json")
VALID_CASES = _DATA["valid_cases"]
FIXED_INSTALLMENT = _DATA["fixed_installments"]
FIXED_BLANK = [FIXED_INSTALLMENT["all_blank"]]

@pytest.mark.calculatornet
@pytest.mark.smoke
class TestRepaymentPositiveCases(BaseTest):
    
    @pytest.mark.parametrize("scenario", VALID_CASES, ids=[s["id"] for s in VALID_CASES])
    def test_monthly_payment_is_correct_for_valid_loans(self, repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"]
        )
        expected = scenario["expected_monthly"]
        cell = repayment_page.monthly_payment_cell(expected)
        
        if cell.count() == 0:
            actual = repayment_page.read_displayed_monthly()
            pytest.fail(
                f"[{scenario['id']}] Expected monthly {expected},"
                f"but repayment calculator displayed, {actual}"
            )
        expect(cell).to_be_visible()
        
    @pytest.mark.parametrize("scenario", VALID_CASES, ids=[s["id"] for s in VALID_CASES])
    def test_total_payment_is_correct_for_valid_loans(self, repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"]
        )
        expected = scenario["expected_total"]
        cell = repayment_page.total_payment_cell(expected)
        
        assert cell.count() > 0 and cell.first.is_visible(), (
            f"[{scenario['id']}] Expected total payment {expected} not displayed."
        )

    @pytest.mark.parametrize("scenario", VALID_CASES, ids=[s["id"] for s in VALID_CASES])
    def test_total_interest_is_correct_for_valid_loans(self, repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"]
        )
        expected = scenario["expected_interest"]
        expect(repayment_page.total_interest_cell(expected)).to_be_visible()
        
    @pytest.mark.parametrize("scenario", FIXED_BLANK, ids=[s["id"] for s in FIXED_BLANK])
    def test_fixed_installment_all_blank_shows_errors(self, repayment_page, scenario):
        repayment_page.fixed_installment_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["fixed_installment"],
        )
        assert repayment_page.has_validation_error(scenario["expected_error"])

            
        