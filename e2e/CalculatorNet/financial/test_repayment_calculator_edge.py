import pytest
from playwright.sync_api import expect
from common.base.base_test import BaseTest
from common.utils.data_loader import load_test_data

_DATA = load_test_data("CalculatorNet","financial", "repayment_calculator_data.json")
EDGE_CASES = _DATA["edge_cases"]
EXTRA_CASES = _DATA["extra_cases"]
INVALID_CASES = _DATA["invalid_cases"]
FIXED_INSTALLMENT = _DATA["fixed_installments"]
FIXED_BLANK = [FIXED_INSTALLMENT["all_blank"]]

@pytest.mark.calculatornet
@pytest.mark.edge
class TestRepaymentEdgeCases(BaseTest):
    
    @pytest.mark.parametrize("scenario", INVALID_CASES, ids=[s["id"] for s in INVALID_CASES])
    def test_invalid_loan_amount_shows_validation_error(self,repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"],
            scenario.get("months",0),
        )
        assert repayment_page.has_validation_error(scenario["expected_error"])
    
    @pytest.mark.parametrize("scenario", EDGE_CASES, ids=[s["id"] for s in EDGE_CASES])
    def test_monthly_payment_is_correct_for_edge_cases(self,repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"],
            scenario.get("months",0),
        )
        expected = scenario["expected_monthly"]
        cell = repayment_page.monthly_payment_cell(expected)
        
        if cell.count() == 0:
            actual = repayment_page.read_displayed_monthly()
            pytest.fail(
                f"[{scenario['id']}] Expected monthly {expected}, "
                f"but repayment calculator displayed {actual}"
            )
        expect(cell).to_be_visible()
        
    @pytest.mark.parametrize("scenario", EDGE_CASES, ids=[s["id"] for s in EDGE_CASES])
    def test_total_interest_is_correct_for_edge_cases(self,repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"],
            scenario.get("months",0),
        )
        expected = scenario["expected_interest"]
        expect(repayment_page.total_interest_cell(expected)).to_be_visible()
          
    @pytest.mark.parametrize("scenario", EXTRA_CASES, ids=[s["id"] for s in EXTRA_CASES])
    def test_total_interest_correct_for_years_and_month_term(self, repayment_page, scenario):
        repayment_page.fixed_time_calculate(
            scenario["loan_amount"],
            scenario["annual_interest_rate"],
            scenario["years"],
            scenario.get("months",0),
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
        
    


            
     
        
    