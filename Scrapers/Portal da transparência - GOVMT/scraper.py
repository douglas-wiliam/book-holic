import requests
import pandas
import time


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print(
        f'Tempo decorrido total: {hours} horas, {mins} minutos e {sec} segundos')


start_time = time.time()

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += '@SECLEVEL=1'

headers = {"Cookie": "PHPSESSID=h4kc4omlo2l40l0ibrqd1v56aqr0psmc; TS01ebaa70=0134aeb20d5724c09b636c64e0e6f3d5af2c0e67444c23383784b1d5f5725519d5dfc35b75ccaf81429842b278b8f719226de722dc22173a1c2a95b4ce8389f3e430150777"}
csv = 'SERVIDORES_GOV_MT/pagina_1.csv'

for i in range(101, 3061):
    URL = f'https://consultas.transparencia.mt.gov.br/pessoal/servidores_ativos/resultado_1.php?pg={i}&mes=1&ano=2023'
    print(URL)
    page_access_start_time = time.time()
    page = requests.get(URL, headers=headers)
    page_access_end_time = time.time()
    tables = pandas.read_html(page.text)
    tables[0].to_csv(csv, mode='a', index=False, header=False)
    time_elapsed = page_access_end_time - page_access_start_time
    print(
        f'Tempo decorrido: {time_elapsed} segundos')

end_time = time.time()

time_elapsed = end_time - start_time
time_convert(time_elapsed)
