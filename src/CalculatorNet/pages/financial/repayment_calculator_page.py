from playwright.sync_api import Locator, Page
from common.base.base_page import BasePage

class RepaymentCalculatorPage(BasePage):
    PATH = "repayment-calculator.html"
    
    #parameterized locators
    _MONTHLY_CELL = "//b[normalize-space()='{value}']"
    _TOTAL_CELL = "//td[normalize-space()='{value}']"
    
    #locators
    loan_amount_input: Locator
    interest_rate_input: Locator
    loan_term_years_input: Locator
    loan_term_months_input: Locator
    compound_select: Locator
    payback_select: Locator
    calculate_button: Locator
    validation_error_message: Locator
    monthly_pay_result: Locator
    monthly_pay_row: Locator
    
    def __init__(self, page: Page, base_url: str):
        super().__init__(page, base_url)

        self.loan_amount_input = page.locator("#cloanamount")
        self.interest_rate_input = page.locator("#cinterestrate")
        self.loan_term_years_input = page.locator("#cyears")
        self.loan_term_months_input = page.locator("#cmonths")
        self.compound_select = page.locator("#ccompound")
        self.payback_select = page.locator("#cpayback")
        self.calculate_button = page.get_by_role("button", name="Calculate")
        self.monthly_pay_result = page.get_by_text("Monthly Pay")
        self.fixed_installment_button = page.get_by_text("Repay with a fixed installment")
        self.fixed_installment_input = page.locator("#cpaybackwayamt")
        self.monthly_pay_row = page.locator("//td[contains(.,'Monthly Pay')]/following-sibling::td")
        
    def monthly_payment_cell(self, expected_value: str) -> Locator:
        return self.page.locator(self._MONTHLY_CELL.format(value=expected_value))

    def total_payment_cell(self, expected_value: str) -> Locator:
        return self.page.locator(self._TOTAL_CELL.format(value=expected_value))

    def total_interest_cell(self, expected_value: str) -> Locator:
        return self.page.locator(self._TOTAL_CELL.format(value=expected_value))
    
    def open(self) -> "RepaymentCalculatorPage":
        self.navigate(self.PATH)
        return self

    def set_loan_amount(self, value) -> None:
        self.loan_amount_input.fill(str(value))

    def set_interest_rate(self, value) -> None:
        self.interest_rate_input.fill(str(value))

    def set_loan_term(self, years, months=0) -> None:
        self.loan_term_years_input.fill(str(years))
        self.loan_term_months_input.fill(str(months))
        
    def set_compound_monthly(self) -> None:
        self.compound_select.select_option("monthly")

    def set_payback_monthly(self) -> None:
        self.payback_select.select_option("month")

    def calculate(self) -> None:
        self.calculate_button.click()
        self.monthly_pay_result.wait_for(state="visible")

    def fixed_time_calculate(self, loan_amount, interest_rate, years, months=0) -> None:
        self.open()
        self.set_loan_amount(loan_amount)
        self.set_interest_rate(interest_rate)
        self.set_loan_term(years, months)
        self.set_compound_monthly()
        self.set_payback_monthly()
        self.calculate()
        
    def read_displayed_monthly(self) -> str:
        try:
            return self.monthly_pay_row.first.inner_text().strip()
        except Exception:
            return "(could not read monthly value)"

    def switch_to_fixed_installment(self) -> None:
        self.fixed_installment_button.click()
        
    def set_fixed_installment(self, value) -> None:
        self.fixed_installment_input.fill(str(value))
        
    def fixed_installment_calculate(self, loan_amount, interest_rate, installment) -> None:
        self.open()
        self.switch_to_fixed_installment()          
        self.set_loan_amount(loan_amount)           
        self.set_interest_rate(interest_rate)
        self.set_fixed_installment(installment)      
        self.calculate_button.click()

    def loan_payments_cell(self, expected: str):
        return self.page.get_by_text(expected)
    
    def has_validation_error(self, expected) -> bool:
        messages = expected if isinstance(expected, list) else [expected]
        return all(
            self.page.get_by_text(msg, exact=False).first.is_visible()
            for msg in messages
        )

        
