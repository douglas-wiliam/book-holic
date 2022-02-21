class color:
    BOLD = '\033[1m'
    END = '\033[0m'


class month:

    def get_month_acronyme(month_name):
        if(month_name.upper() == "JANEIRO"):
            return "JAN"
        elif(month_name.upper() == "FEVEREIRO"):
            return "FEV"
        elif(month_name.upper() == "MARÇO"):
            return "MAR"
        elif(month_name.upper() == "ABRIL"):
            return "ABR"
        elif(month_name.upper() == "MAIO"):
            return "MAIO"
        elif(month_name.upper() == "JUNHO"):
            return "JUN"
        elif(month_name.upper() == "JULHO"):
            return "JUL"
        elif(month_name.upper() == "AGOSTO"):
            return "AGO"
        elif(month_name.upper() == "SETEMBRO"):
            return "SET"
        elif(month_name.upper() == "OUTUBRO"):
            return "OUT"
        elif(month_name.upper() == "NOVEMBRO"):
            return "NOV"
        elif(month_name.upper() == "DEZEMBRO"):
            return "DEZ"
        else:
            return ""
