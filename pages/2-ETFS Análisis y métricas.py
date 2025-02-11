import streamlit as st
import yfinance as yf
import pandas as pd
import base64
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
import warnings
warnings.simplefilter("ignore", category=FutureWarning)
# Suprimir advertencias ValueWarning
warnings.simplefilter("ignore")

# Configuración de Streamlit
st.set_page_config(page_title="Analisis de ETFS", page_icon="img/logo2.png", layout="wide")

theme_plotly = None

#"""" codigo de particulas que se agregan en le background""""
particles_js = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Particles.js</title>
  <style>
  #particles-js {
    background-color: #191970;    
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: 0;
    left: 0;
    z-index: -1; /* Send the animation to the back */
  }
  .content {
    position: relative;
    z-index: 1;
    color: white;
  }
  
</style>
</head>
<body>
  <div id="particles-js"></div>
  <div class="content">
    <!-- Placeholder for Streamlit content -->
  </div>
  <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
  <script>
    particlesJS("particles-js", {
      "particles": {
        "number": {
          "value": 300,
          "density": {
            "enable": true,
            "value_area": 800
          }
        },
        "color": {
          "value": "#fffc33"
        },
        "shape": {
          "type": "circle",
          "stroke": {
            "width": 0,
            "color": "#000000"
          },
          "polygon": {
            "nb_sides": 5
          },
          "image": {
            "src": "img/github.svg",
            "width": 100,
            "height": 100
          }
        },
        "opacity": {
          "value": 0.5,
          "random": false,
          "anim": {
            "enable": false,
            "speed": 1,
            "opacity_min": 0.2,
            "sync": false
          }
        },
        "size": {
          "value": 2,
          "random": true,
          "anim": {
            "enable": false,
            "speed": 40,
            "size_min": 0.1,
            "sync": false
          }
        },
        "line_linked": {
          "enable": true,
          "distance": 100,
          "color": "#fffc33",
          "opacity": 0.22,
          "width": 1
        },
        "move": {
          "enable": true,
          "speed": 0.2,
          "direction": "none",
          "random": false,
          "straight": false,
          "out_mode": "out",
          "bounce": true,
          "attract": {
            "enable": false,
            "rotateX": 600,
            "rotateY": 1200
          }
        }
      },
      "interactivity": {
        "detect_on": "canvas",
        "events": {
          "onhover": {
            "enable": true,
            "mode": "grab"
          },
          "onclick": {
            "enable": true,
            "mode": "repulse"
          },
          "resize": true
        },
        "modes": {
          "grab": {
            "distance": 100,
            "line_linked": {
              "opacity": 1
            }
          },
          "bubble": {
            "distance": 400,
            "size": 2,
            "duration": 2,
            "opacity": 0.5,
            "speed": 1
          },
          "repulse": {
            "distance": 200,
            "duration": 0.4
          },
          "push": {
            "particles_nb": 2
          },
          "remove": {
            "particles_nb": 3
          }
        }
      },
      "retina_detect": true
    });
  </script>
</body>
</html>
"""
globe_js = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vanta Globe Animation</title>
    <style type="text/css">
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        overflow: hidden;
        height: 100%;
        margin: 0;
        background-color: #1817ed; /* Fondo azul */
      }
      #canvas-globe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="canvas-globe"></div>       

    <!-- Scripts de Three.js y Vanta.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanta/0.5.24/vanta.globe.min.js"></script>

    <script type="text/javascript">      
      document.addEventListener("DOMContentLoaded", function() {
        VANTA.GLOBE({
          el: "#canvas-globe", // El elemento donde se renderiza la animación
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200.00,
          minWidth: 200.00,
          scale: 1.00,
          scaleMobile: 1.00,
          color: 0xd1ff3f, // Color verde amarillento
          backgroundColor: 0x1817ed // Fondo azul
        });
      });
    </script>
  </body>
</html>
"""
waves_js = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vanta Waves Animation</title>
    <style type="text/css">
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      html, body {
        height: 100%;
        margin: 0;
        overflow: hidden;
      }
      #canvas-dots {
        position: absolute;
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  <body>
    <div id="canvas-waves"></div>       
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vanta/0.5.24/vanta.waves.min.js"></script>
    
    <script type="text/javascript">      
      document.addEventListener("DOMContentLoaded", function() {
        VANTA.WAVES({
          el: "#canvas-waves", // Especificar el contenedor donde debe renderizarse
           mouseControls: true,
           touchControls: true,
           gyroControls: false,
           minHeight: 200.00,
           minWidth: 200.00,
           scale: 1.00,
           scaleMobile: 1.00,
           color: 0x15159b
        });
      });
    </script>
  </body>
</html>
"""

#""" imagen de background"""
def add_local_background_image(image):
  with open(image, "rb") as image:
    encoded_string = base64.b64encode(image.read())
    st.markdown(
      f"""
      <style>
      .stApp{{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
      }}    
      </style>
      """,
      unsafe_allow_html=True
    )
add_local_background_image("img/fondo.jpg")

#""" imagen de sidebar"""
def add_local_sidebar_image(image):
  with open(image, "rb") as image:
    encoded_string = base64.b64encode(image.read())
    st.markdown(
      f"""
      <style>
      .stSidebar{{
        background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
      }}    
      </style>
      """,
      unsafe_allow_html=True
    )

add_local_sidebar_image("img/fondo1.jpg")

with st.container():
    #st.write("---")
    left, midle ,right = st.columns(3, gap='small', vertical_alignment="center")
    with left:
        components.html(waves_js, height=100,scrolling=False)
    with midle:
        components.html(globe_js, height=100,scrolling=False) 
    with right:
       components.html(particles_js, height=100,scrolling=False) 
    #st.write("---")    

#-------------- animacion con css de los botones modelo Arima ------------------------
with open('style/style.css') as f:
        css = f.read()
        
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.logo(image="img/market.png",size='large')


st.button(' --- Listado de ETFs ---', key='grafico', use_container_width=True )
with st.container(border=True):
    col1 ,col2 = st.columns(2, gap="small", vertical_alignment="top", border=True)    
    with col1:
        st.text('XLE - Energy Select Sector SPDR Fund: Sigue las empresas del sector energético en EE.UU., incluyendo las de petróleo, gas y energías renovables.')
        st.text('XLF - Financial Select Sector SPDR Fund: Representa a las empresas del sector financiero, como bancos, compañías de inversión y seguros.')
        st.text('XLU - Utilities Select Sector SPDR Fund: Incluye empresas de servicios públicos, como electricidad y agua.')
        st.text('XLI - Industrial Select Sector SPDR Fund: Se compone de empresas industriales, incluyendo construcción, fabricación y transporte.')
        st.text('GDX - VanEck Gold Miners ETF: Incluye compañías mineras de oro a nivel global, proporcionando exposición al sector de la minería de oro.')
        st.text('XLK - Technology Select Sector SPDR Fund: Agrupa a empresas del sector tecnológico, incluyendo hardware, software y servicios de información.')
        st.text('XLV - Health Care Select Sector SPDR Fund: Este ETF incluye empresas del sector de la salud, como farmacéuticas y equipos médicos.')
        st.text('XLY - Consumer Discretionary Select Sector SPDR Fund: Cubre empresas de bienes de consumo discrecional, como minoristas, automóviles y servicios de ocio.')
        st.text('XLP - Consumer Staples Select Sector SPDR Fund: Invierte en empresas de productos de consumo básico, como alimentos, bebidas y productos domésticos.')
        st.text('XLB - Materials Select Sector SPDR Fund: Contiene empresas del sector de materiales, que incluye químicos, construcción y empaques.')
        st.text('XOP - Spdr S&P Oil & Gas Exploration & Production ETF: Se enfoca en compañías de exploración y producción de petróleo y gas.')
        st.text('IYR - iShares U.S. Real Estate ETF: Proporciona exposición a propiedades y bienes raíces de EE.UU., incluyendo REITs.')

        
    with col2:
        st.text('XHB - Spdr S&P Homebuilders ETF: Incluye empresas relacionadas con la construcción de viviendas, desde constructores hasta proveedores de materiales.')
        st.text('ITB - iShares U.S. Home Construction ETF: Similar al XHB, este ETF se enfoca en constructores de viviendas y proveedores.')
        st.text('VNQ - Vanguard Real Estate Index Fund ETF Shares: Ofrece exposición al sector inmobiliario y a REITs, similar al IYR.')
        st.text('GDXJ - VanEck Junior Gold Miners ETF: Agrupa a pequeñas y medianas empresas de minería de oro y metales preciosos.')
        st.text('IYE - iShares U.S. Energy ETF: Sigue a empresas del sector energético en EE.UU., parecido al XLE pero con posiblemente una composición ligeramente diferente.')
        st.text('OIH - VanEck Oil Services ETF: Se centra en empresas que proporcionan servicios y equipos para la industria petrolera.')
        st.text('XME - SPDR S&P Metals & Mining ETF: Incluye compañías involucradas en la extracción y procesamiento de metales y minerales.')
        st.text('XRT - Spdr S&P Retail Etf: Se enfoca en el sector minorista, incluyendo tiendas de diferentes tipos y tamaños.')
        st.text('SMH - VanEck Semiconductor ETF: Proporciona exposición a la industria de semiconductores, incluyendo fabricantes y diseñadores de chips.')
        st.text('IBB - iShares Biotechnology ETF: Incluye empresas biotecnológicas y farmacéuticas enfocadas en el desarrollo de medicamentos y terapias.')
        st.text('KBE - SPDR S&P Bank ETF: Se compone de bancos de diferentes tamaños, desde multinacionales hasta bancos regionales.')
        st.text('KRE - SPDR S&P Regional Banking ETF: Similar al KBE pero enfocado en bancos regionales y pequeños de EE.UU.')
        st.text('XTL - SPDR S&P Telecom ETF: XTL - SPDR S&P Telecom ETF: Este ETF se centra en el sector de las telecomunicaciones, incluyendo empresas que proporcionan servicios de telecomunicaciones, como telefonía móvil, fija, internet y televisión por cable.')

etfs = [
    'XLE', 'XLF', 'XLU', 'XLI', 'GDX', 'XLK', 'XLV', 'XLY', 'XLP', 'XLB', 
    'XOP', 'IYR', 'XHB', 'ITB', 'VNQ', 'GDXJ', 'IYE', 'OIH', 'XME', 'XRT', 
    'SMH', 'IBB', 'KBE', 'KRE', 'XTL'
]
start_date = '2022-01-01'
end_date = '2025-03-01'

data = yf.download(etfs, start=start_date, end=end_date)['Close']


returns = data.pct_change().dropna()  #NAN #Null

# Obtener datos del S&P 500
sp500 = yf.download('^GSPC', start=start_date, end=end_date)['Close']
sp500_returns = sp500.pct_change().dropna()

correlation_returns = returns.corr()

#Prepararnos para graficar

with st.expander("Desplegar Correlación de retornos diarios ETFs"):
        plt.figure(figsize=(14, 12))
        #sns.heatmap(correlation_returns, annot=True, fmt=".2f", cmap='coolwarm')
        sns.heatmap(correlation_returns, annot=True, fmt=".2f", cmap='crest')
        plt.title(f'Correlación de los retornos diarios de los ETFs seleccionados desde {start_date}')

        plt.xticks(rotation=45)
        plt.yticks(rotation=45)

        plt.tight_layout()

        st.pyplot(plt)

with st.expander("Desplegar Gráfica de Beta cada ETFs y S&P500 -histograma de rendimientos"):
# Calcular beta (regresión) de cada ETF con respecto al S&P 500
    betas = []
    for etf in etfs:
        y = returns[etf]  # Retornos del ETF
        x = sp500_returns  # Retornos del S&P 500
        
        # Regresión lineal (Y = alpha + beta * X)
        x = sm.add_constant(x)  # Agregar constante (intercepto)
        model = sm.OLS(y, x).fit()
        betas.append(model.params[1])  # El coeficiente de X es la beta

    beta_df = pd.DataFrame({'ETF': etfs, 'Beta': betas})

    # Graficar beta de los ETFs
    plt.figure(figsize=(12, 8))
    sns.barplot(x='ETF', y='Beta', data=beta_df, palette='coolwarm')
    plt.title('Beta de los ETFs en relación con el S&P 500')
    plt.tight_layout()
    st.pyplot(plt)

    # Histograma de los retornos de cada ETF
    plt.figure(figsize=(14, 10))

    # Número de filas y columnas para los subgráficos
    num_etfs = len(etfs)
    cols = 4
    rows = (num_etfs // cols) + 1  # Ajustar el número de filas

    for i, etf in enumerate(etfs):
        plt.subplot(rows, cols, i+1)
        sns.histplot(returns[etf], kde=True, bins=30, color='blue', stat='density')
        plt.title(f'Histograma de Retornos - {etf}')
        plt.xlabel('Retornos Diarios')
        plt.ylabel('Densidad')

    plt.tight_layout()
    st.pyplot(plt)

with st.expander("Desplegar Volatilidad Anualizada/Sharpe Ratio de ETFs"): 
    # Volatilidad anualizada
        volatility = returns.std() * np.sqrt(252)  # 252 días de trading en un año

        plt.figure(figsize=(12, 8))
        sns.barplot(x=volatility.index, y=volatility.values, palette='viridis')
        plt.title('Volatilidad Anualizada de los ETFs')
        plt.xlabel('ETF')
        plt.ylabel('Volatilidad Anualizada')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)

        # Calcular el Sharpe Ratio
        risk_free_rate = 0.05  # Tasa libre de riesgo (supongamos 3% anual)
        excess_returns = returns.mean() - risk_free_rate / 252  # Exceso de retornos sobre la tasa libre de riesgo diaria
        sharpe_ratio = excess_returns / returns.std() * np.sqrt(252)  # Sharpe Ratio anualizado

        plt.figure(figsize=(12, 8))
        sns.barplot(x=sharpe_ratio.index, y=sharpe_ratio.values, palette='magma')
        plt.title('Sharpe Ratio de los ETFs')
        plt.xlabel('ETF')
        plt.ylabel('Sharpe Ratio')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)
          
with st.expander("Desplegar Rentabilidad vs Riesgo de ETFs con Regresión Lineal"): 
    # Calcular los rendimientos promedio de cada ETF
    average_returns = returns.mean()
    # Preparar los datos para el gráfico de regresión lineal
    regression_data = pd.DataFrame({
        'Volatilidad': volatility,
        'Rendimiento Promedio': average_returns
    })
  
    plt.figure(figsize=(10, 6))
    
    x = regression_data['Volatilidad']
    y = regression_data['Rendimiento Promedio']
    
    # Ajustar el modelo de regresión
    model = sm.OLS(y, sm.add_constant(x)).fit()
    predictions = model.predict(sm.add_constant(x))
    
    # Graficar el scatterplot y la línea de regresión
    sns.scatterplot(x=x, y=y, color='blue', label='Datos')
    plt.plot(x, predictions, color='red', label='Reg.-lineal')
    
    # Agregar los tickers como etiquetas en los puntos
    for i, etf in enumerate(etfs):
        plt.text(x[i], y[i], etf, fontsize=9, ha='right', color='black')

    plt.title('Regresión Lineal: Volatilidad vs Rendimientos Promedio de ETFs')
    plt.xlabel('Volatilidad (Desviación estándar de retornos diarios)')
    plt.ylabel('Rendimiento Promedio')
    plt.legend()
    plt.tight_layout()
    st.pyplot(plt)
        
with st.expander("Desplegar Frontera Eficiencia para 5 ETFs"): 
    st.warning("Considerar que a mayor plazo de tiempo y variar la tasa de riesgo mayor, hace que el modelo se demore en el calculo muchos o varios segudos. Teniendo que esperar para el despliegue de Gráfico e cuadro de información")    
# Función para descargar datos históricos
    def get_stock_data(tickers, start_date, end_date):
        data = pd.DataFrame()
        for ticker in tickers:
            etfs_data = yf.download(ticker, start=start_date, end=end_date)['Close']
            data[ticker] = etfs_data
        return data

    # Entrada de datos por parte del usuario
    with st.container(border=True):
        col1, col2,col3 = st.columns(3, gap='small',vertical_alignment="top", border=True) 
    with col1:
        tickers_input = st.text_input(f"Ingrese 5 ETFs (separados por comas y mayúsculas)", "XLI, XLK, IBB, XOP, XRT").upper()
        tickers = [ticker.strip() for ticker in tickers_input.split(',')][:5]
    with col2:
        start_date = st.date_input("Fecha de inicio", value=pd.to_datetime('2022-01-01'), help="ingrese fecha que sea igual o menor a 10 años")
        end_date = st.date_input("Fecha de fin", value=pd.to_datetime('2025-03-01'), help="puede colocar fecha superior a la fecha actual")
    with col3:
        rf_rate = float(st.number_input("digite tasa de libre riesgo (Valor Porcentual ej. 4.5)", min_value=0.5, max_value=15.5, step=0.5, value=4.5, help="por ej.4.5% "))/100


    if st.button("Ejecutar cálculo de Frontera de Eficiencia", key="glow-on-reg"):
            # Convertir los retornos a anualizados
            # Obtener datos
            etfs_date = get_stock_data(tickers, start_date, end_date)
            # Calcular retornos diarios
            returns = etfs_date.pct_change().dropna() #Retornos simples        
            # Parámetros para la simulación de Monte Carlo
            num_portfolios = 1000            
            #st.write(returns)
            # Arrays para almacenar los resultados de la simulación
            all_weights = np.zeros((num_portfolios, len(tickers)))
            ret_arr = np.zeros(num_portfolios)
            vol_arr = np.zeros(num_portfolios)
            sharpe_arr = np.zeros(num_portfolios)

            # Simulación de Monte Carlo
            for port in range(num_portfolios):
                # Generar pesos aleatorios para los ETFs
                weights = np.random.random(len(tickers))
                weights = weights / np.sum(weights)  # Normalización de los pesos
                all_weights[port, :] = weights
                
                # Calcular el retorno esperado del portafolio (anualizado)
                port_ret = np.sum(returns.mean() * weights)  # Rentabilidad anualizada
                ret_arr[port] = port_ret
                
                # Calcular la volatilidad del portafolio (anualizada)
                port_vol = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))  # Volatilidad anualizada
                vol_arr[port] = port_vol
                
                # Calcular el Ratio de Sharpe
                sharpe_arr[port] = (port_ret - rf_rate) / port_vol

            # Encontrar el portafolio óptimo (mayor Sharpe Ratio)
            optimal_idx = sharpe_arr.argmax()
            optimal_weights = all_weights[optimal_idx, :]
            optimal_ret = ret_arr[optimal_idx]
            optimal_vol = vol_arr[optimal_idx]
            optimal_sharpe = sharpe_arr[optimal_idx]

            # Crear un DataFrame con los resultados
            results = pd.DataFrame({
                'Return': ret_arr,
                'Volatility': vol_arr,
                'Sharpe Ratio': sharpe_arr
            })

            # Visualización de los resultados
            plt.figure(figsize=(15, 8))
            plt.scatter(vol_arr, ret_arr, c=sharpe_arr, cmap='viridis', marker='o', s=10)
            plt.colorbar(label='Sharpe Ratio')
            plt.scatter(optimal_vol, optimal_ret, color='red', marker='*', s=200, label='Portafolio Óptimo')
            plt.xlabel('Volatilidad Anualizada')
            plt.ylabel('Retorno Esperado Anualizado')
            plt.title('Resultados de la Optimización de Portafolio - Simulación de Monte Carlo')
            plt.legend()
            st.pyplot(plt)

            # Imprimir los resultados del portafolio óptimo
            with st.container():
                col1, col2 = st.columns(2, gap='medium', vertical_alignment="top")
                with col1:
                    st.subheader(f"Tasa de Libre Riesgo: {rf_rate*100:.2f} % anual")
                    st.write("---")
                    st.subheader("\nInformación del Portafolio Óptimo:")
                    st.subheader(f"Retorno Esperado: {optimal_ret * 100:.2f}% anual")
                    st.subheader(f"Volatilidad: {optimal_vol * 100:.2f}% anual")
                    st.subheader(f"Ratio de Sharpe: {optimal_sharpe:.2f}")
                with col2:
                    st.subheader("\nParticipación % óptima de los ETFs:")
                    for stock, weight in zip(etfs, optimal_weights):
                        st.subheader(f"{stock}: {weight * 100:.2f}%")


# --------------- footer -----------------------------
st.write("---")
with st.container():
  #st.write("---")
  st.write("&copy; - derechos reservados -  2024 -  Walter Gómez - FullStack Developer - Data Science - Business Intelligence")
  #st.write("##")
  left, right = st.columns(2, gap='medium', vertical_alignment="bottom")
  with left:
    #st.write('##')
    st.link_button("Mi LinkedIn", "https://www.linkedin.com/in/walter-gomez-fullstack-developer-datascience-businessintelligence-finanzas-python/",use_container_width=True)
  with right: 
     #st.write('##') 
    st.link_button("Mi Porfolio", "https://walter-portfolio-animado.netlify.app/", use_container_width=True)
      
