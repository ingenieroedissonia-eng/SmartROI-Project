# 🤖 SmartROI v2.0 | AI-Powered Analyzer

**Sistema de Ingeniería IA Aplicada al Comercio (M.A.I.I.E.)**

> *Sistema de Soporte a la Decisión (DSS) diseñado para evaluar la viabilidad financiera de operaciones de importación mediante simulación de escenarios, métricas de rentabilidad y reglas de decisión automatizadas.*

---

## 🎯 Descripción del Proyecto
SmartROI v2.0 es un **Asistente Inteligente de Negocios** enfocado en comercio internacional.  
Permite a importadores, analistas y emprendedores evaluar rápidamente la rentabilidad de un producto, considerando costos, impuestos, márgenes y retorno de inversión (ROI).

El sistema no solo calcula, sino que interpreta los resultados y entrega un **veredicto estratégico**, simulando el razonamiento de un asesor financiero mediante reglas de decisión claras.

## 🛠️ Tecnologías Utilizadas
* **Python 3.10+**: Lenguaje principal para la lógica de negocio y cálculos financieros.
* **Streamlit**: Framework para el desarrollo de la interfaz web interactiva (Data Apps / SaaS).
* **Pandas**: Estructuración de datos y soporte para visualización.
* **Git & GitHub**: Control de versiones y publicación del proyecto.

## ✨ Funcionalidades Clave

### 1️⃣ Simulación Financiera
Cálculo automático de:
* Subtotal de inversión
* Impuestos de importación (15%)
* Inversión total
* Ventas proyectadas
* Ganancia neta
* ROI (%)

### 2️⃣ Motor de Decisión (IA Simbólica)
Clasificación automática de la inversión según el ROI calculado:
* 🌟 **Oportunidad Elite** → ROI ≥ 40%
* ✅ **Negocio Viable** → ROI ≥ 15%
* ⚠️ **Alto Riesgo** → ROI < 15%

*Este enfoque simula un sistema experto basado en reglas, base conceptual de la Inteligencia Artificial.*

### 3️⃣ Visualización de Datos
* KPIs financieros en tiempo real.
* Gráficos comparativos (Inversión vs. Ganancia).
* Tabla detallada de métricas clave.
* Alertas visuales según nivel de riesgo.

---

## 💻 Ejecución Local del Proyecto

Sigue estos pasos para ejecutar SmartROI v2.0 en tu entorno local:

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/ingenieroedissonia-eng/SmartROI-Project.git

   pip install streamlit pandas
   streamlit run app.py
   La aplicación se abrirá automáticamente en tu navegador web.
