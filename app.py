import streamlit as st
import pandas as pd

# =====================================================
# 1. CONFIGURACIÓN GENERAL DE LA PÁGINA
# =====================================================
st.set_page_config(
    page_title="SmartROI AI | M.A.I.I.E.",
    page_icon="🤖",
    layout="centered"
)

# =====================================================
# 2. ENCABEZADO Y PRESENTACIÓN
# =====================================================
st.title("🤖 SmartROI v2.0 | AI-Powered Analyzer")
st.markdown("### 🚀 Sistema de Ingeniería IA Aplicada al Comercio")
st.markdown("**Desarrollado por:** Ing. Edisson A.G.C. | **Modelo:** M.A.I.I.E.")
st.markdown("---")

# =====================================================
# 3. BARRA LATERAL (SIDEBAR) - INPUTS
# =====================================================
st.sidebar.header("🔧 Parámetros de Simulación")
st.sidebar.info("Ingrese los datos del producto para calcular la viabilidad de importación.")

costo = st.sidebar.number_input(
    "Costo Unitario (USD)",
    min_value=0.0,
    value=100.0,
    format="%.2f"
)

precio = st.sidebar.number_input(
    "Precio de Venta (USD)",
    min_value=0.0,
    value=200.0,
    format="%.2f"
)

cantidad = st.sidebar.number_input(
    "Cantidad a Importar",
    min_value=1,
    value=10,
    step=1
)

tasa_arancel = 0.15  # 15% Tasa estándar tecnológica

# =====================================================
# 4. LÓGICA DE NEGOCIO (EL CEREBRO)
# =====================================================
if st.sidebar.button("EJECUTAR ANÁLISIS ⚡"):

    # --- 4.1 MOTOR DE CÁLCULO ---
    subtotal = costo * cantidad
    impuestos = subtotal * tasa_arancel
    inversion_total = subtotal + impuestos

    ventas_totales = precio * cantidad
    ganancia_neta = ventas_totales - inversion_total

    # Cálculo seguro del ROI
    if inversion_total > 0:
        roi = (ganancia_neta / inversion_total) * 100
    else:
        roi = 0

    # --- 4.2 MOTOR DE DECISIÓN (SISTEMA EXPERTO) ---
    if roi >= 40:
        veredicto = "🌟 OPORTUNIDAD ELITE (Alta Rentabilidad)"
        estado = "success"
    elif roi >= 15:
        veredicto = "✅ NEGOCIO VIABLE (Rentabilidad Normal)"
        estado = "warning"
    else:
        veredicto = "⚠️ ALTO RIESGO (No Recomendado)"
        estado = "error"

    # =================================================
    # 5. DASHBOARD DE RESULTADOS (VISUALIZACIÓN)
    # =================================================
    st.markdown("### 📊 Reporte Financiero & Estratégico")

    # Métricas KPI (Key Performance Indicators)
    col1, col2, col3 = st.columns(3)
    col1.metric("Inversión Total", f"${inversion_total:,.2f}")
    col2.metric("Ventas Proyectadas", f"${ventas_totales:,.2f}")
    col3.metric("ROI (Retorno)", f"{roi:.2f}%", delta_color="normal")

    # Banner de Veredicto
    if estado == "success":
        st.success(f"**VEREDICTO IA:** {veredicto}")
    elif estado == "warning":
        st.warning(f"**VEREDICTO IA:** {veredicto}")
    else:
        st.error(f"**VEREDICTO IA:** {veredicto}")

    # Advertencia financiera si hay pérdida
    if ganancia_neta < 0:
        st.info("📉 **Nota Técnica:** Este escenario proyecta pérdidas financieras. Se sugiere renegociar costos.")

    # =================================================
    # 6. GRÁFICOS Y TABLAS
    # =================================================
    st.divider()
    
    # 6.1 Gráfico de Barras
    st.markdown("#### 📉 Comparativa: Inversión vs. Ganancia")
    datos_grafico = pd.DataFrame({
        "Concepto": ["Inversión Total", "Ganancia Neta"],
        "Monto (USD)": [inversion_total, ganancia_neta]
    })
    st.bar_chart(datos_grafico.set_index("Concepto"), use_container_width=True)

    # 6.2 Tabla de Detalles (Dataframe)
    with st.expander("📂 Ver Tabla de Datos Detallada"):
        st.dataframe({
            "Métrica": ["Costo Unitario", "Impuestos (15%)", "Costo Total Importación", "Precio Venta", "Margen Neto"],
            "Valor": [costo, impuestos, inversion_total, precio, ganancia_neta]
        })

    # =================================================
    # 7. PIE DE PÁGINA (BRANDING)
    # =================================================
    st.markdown("---")
    st.caption("© 2025 Edisson A.G.C. | Ecosistema M.A.I.I.E. | Ingeniería IA Aplicada al Comercio")