import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="PetMatch | e-Commerce", page_icon="🐾", layout="wide")

# --- NUEVO: Inicializar el Carrito en la Memoria de Sesión ---
if 'carrito' not in st.session_state:
    st.session_state.carrito = []

# 2. Simulación de los registros
inventario_petmatch = [
    {
        "id_item": "uuid-101",
        "tipo_oferta": "Producto",
        "nombre": "Alimento Hipoalergénico Salmón",
        "especie_objetivo": "Perro",
        "precio": 45000,
        "requiere_reserva": False,
        "stock_disponible": 15,
        "imagen": "https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=60"
    },
    {
        "id_item": "uuid-102",
        "tipo_oferta": "Servicio",
        "nombre": "Paseo y Adiestramiento Conductual",
        "especie_objetivo": "Perro",
        "precio": 15000,
        "requiere_reserva": True,
        "stock_disponible": 5,
        "imagen": "https://tn.com.ar/resizer/v2/bethany-lane-fundadora-del-whistle-wag-un-servicio-de-paseo-para-perros-en-new-york-asegura-que-gana-mas-de-100000-dolares-al-ano-foto-ilustrativa-3ZMKD4PH4BFIRFGO7CYQKY6NAA.jpg?auth=3d66fc7d287b11211e256031e5059d3487730d933c8c5ef0da24a5ab338febb1&width=1440"
    },
    {
        "id_item": "uuid-103",
        "tipo_oferta": "Producto",
        "nombre": "Torre Rascador Multinivel Premium",
        "especie_objetivo": "Gato",
        "precio": 85000,
        "requiere_reserva": False,
        "stock_disponible": 3,
        "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcStkdGnK2zc1_rJPDmn4AY2UCkMvQ19cgJVBQdxKG7QJ7n7zz6oUTw_DDUq&s=10"
    },
    {
        "id_item": "uuid-104",
        "tipo_oferta": "Servicio",
        "nombre": "Consulta Nutricional Online",
        "especie_objetivo": "Gato/Perro",
        "precio": 12000,
        "requiere_reserva": True,
        "stock_disponible": 10,
        "imagen": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQ2RbdMSX1ilxNTdFjdLl219yC_ezVSpjcDTbDkamM_ENlFihsRGL1q5s&s=10"
    }
]

# --- NUEVO: Panel Lateral (Sidebar) para ver el Carrito ---
with st.sidebar:
    st.header("🛒 Tu Carrito")
    if len(st.session_state.carrito) == 0:
        st.write("El carrito está vacío.")
    else:
        total = 0
        for item in st.session_state.carrito:
            st.write(f"- {item['nombre']} (**${item['precio']:,}**)")
            total += item['precio']
        st.divider()
        st.subheader(f"Total: ${total:,}")
        if st.button("Proceder al pago", type="primary"):
            st.success("¡Simulación de compra exitosa!")
            st.session_state.carrito = [] # Vaciar carrito
            st.rerun()

# 3. Interfaz de Usuario (UI) Principal
st.title("🐾 PetMatch")
st.markdown("### Match perfecto para tu mascota")
st.write("Productos y servicios hiperpersonalizados basados en el perfil de tu compañero.")
st.divider()

col1, col2 = st.columns(2)

for index, item in enumerate(inventario_petmatch):
    with col1 if index % 2 == 0 else col2:
        with st.container(border=True):
            st.image(item["imagen"], use_container_width=True)
            
            if item["tipo_oferta"] == "Servicio":
                st.markdown("🟣 **SERVICIO**")
            else:
                st.markdown("🟢 **PRODUCTO**")
            
            st.subheader(item["nombre"])
            st.write(f"**Ideal para:** {item['especie_objetivo']}")
            st.metric(label="Precio", value=f"${item['precio']:,.0f}".replace(",", "."))
            
            # --- NUEVO: Lógica funcional de los botones ---
            if item["requiere_reserva"]:
                st.write(f"📅 *Cupos disponibles: {item['stock_disponible']}*")
                if st.button("Reservar Turno", key=f"btn_{item['id_item']}", type="primary"):
                    st.session_state.carrito.append(item)
                    st.toast(f"¡Turno para {item['nombre']} reservado!")
            else:
                st.write(f"📦 *Stock disponible: {item['stock_disponible']} u.*")
                if st.button("Añadir al Carrito", key=f"btn_{item['id_item']}"):
                    st.session_state.carrito.append(item)
                    st.toast(f"¡{item['nombre']} añadido al carrito!")