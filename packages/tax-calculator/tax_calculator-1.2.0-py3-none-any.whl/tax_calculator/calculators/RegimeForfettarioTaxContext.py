from tax_calculator.ITaxContext import StandardTaxContext
from tax_calculator.calculators.CodiceAteco import CodiceAteco


class RegimeForfettarioTaxContext(StandardTaxContext):

    def __init__(self):
        super().__init__()

        self.codice_ateco: CodiceAteco = None
        self.coefficiente_di_redditivita_percentage: float = None
        self.ricavi_money: float = None
        self.contributi_previdenziali_anno_scorso_money: float = None
        self.aliquota_imposta_sostitutiva_percentage: float = None
        self.contributi_previdenziali_percentage: float = None

    def help_codice_ateco(self) -> str:
        return """Il codice ateco della tua attivita.
        """

    def help_coefficiente_di_redditivita_percentage(self) -> str:
        return """Coeficciente di reddività of your company. useful if you don't know your codice ATECO. Mutually 
        exclusive with codice ateco. 
        """

    def help_ricavi_money(self) -> str:
        return """
        I tuoi ricavi annuali
        """

    def help_contributi_previdenziali_percentage(self) -> str:
        """
        A percentage of the reddito imponibile lordo representing the amount of money
        you need to give to INPS or similia.
        :return:
        """

    def help_contributi_previdenziali_anno_scorso_money(self) -> str:
        return """
        Contributi previdenziali pagati l'anno scorso
        """

    def help_aliquota_imposta_sostitutiva_percentage(self) -> str:
        return """
        Aliquota sostitutiva. per le attività appena aperte è del 5%,
        per le altre del 15%
        """








