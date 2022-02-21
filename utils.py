class color:
    BOLD = '\033[1m'
    END = '\033[0m'


class month:

    def get_month_acronyme(month_name):
        if(month_name.upper() == "JANEIRO"):
            return "jan."
        elif(month_name.upper() == "FEVEREIRO"):
            return "fev."
        elif(month_name.upper() == "MARÇO" or month_name.upper() == "MARCO"):
            return "mar."
        elif(month_name.upper() == "ABRIL"):
            return "abr."
        elif(month_name.upper() == "MAIO"):
            return "maio"
        elif(month_name.upper() == "JUNHO"):
            return "jun."
        elif(month_name.upper() == "JULHO"):
            return "jul."
        elif(month_name.upper() == "AGOSTO"):
            return "ago."
        elif(month_name.upper() == "SETEMBRO"):
            return "set."
        elif(month_name.upper() == "OUTUBRO"):
            return "out."
        elif(month_name.upper() == "NOVEMBRO"):
            return "nov."
        elif(month_name.upper() == "DEZEMBRO"):
            return "dez."
        else:
            return "NOME DE MÊS INVÁLIDO"
