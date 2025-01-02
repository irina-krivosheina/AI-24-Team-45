import os
import streamlit as st

st.title("Exploratory Data Analysis (EDA)")

st.header("Общая информация UA-DETRAC-DATASET")
st.write("""
- **Количество изображений в датасете**: 83,756
- **Количество объектов в датасете**: 992,180
- **Среднее количество объектов на изображение**: 12
""")

st.header("Класс объекта")
st.write("""
- **1. bicycle**
- **2. motorcycle**
- **3. car**
- **4. transporter (van)**
- **5. bus**
- **6. truck (others)**
- **7. trailer - no instance of it in the dataset**
- **8. unknown**
- **9. mask**
""")
st.write("""
Каждая аннотация связывает объекты с их расположением на изображении и классифицирует их по соответствующему типу.
""")
st.info(
    "Данная аннотация является улучшенной версией стандартной аннотации UA-DETRAC и находится в общем доступе по "
    "[ссылке](https://www.kaggle.com/datasets/patrikskalos/ua-detrac-fix-masks-two-wheelers). "
    "В стандартной аннотации было только 3 класса."
)

st.header("Распределение объектов разных классов в датасете в процентом соотношении")
st.image(
    "../images/gist.png",
    caption="Распределение объектов"
)
st.write("""
```
bicycle	0.425326
bus	3.388700
car	48.985668
mask	40.374226
motorcycle	0.667520
transporter (van)	5.719023
truck (others)	0.355278
unknown	0.084259
```
""")

st.header("Средний размер (площадь) bbox по классам")
st.write("""
```
bicycle	0.004044
bus	0.061244
car	0.011969
mask	0.029105
motorcycle	0.004762
transporter (van)	0.018848
truck (others)	0.036613
unknown	0.007589
```
""")

st.header("Примеры инференса")
image_folder = "../images"
image_files = [f for f in os.listdir(image_folder) if 'expl_bbox' in f]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    st.image(image_path, caption=image_file)
