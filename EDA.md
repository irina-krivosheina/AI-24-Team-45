# EDA

## Общая информация UA-DETRAC-DATASET:
- **Количество изображений в датасете**: 83,756
- **Количество объектов в датасете**: 992,180
- **Среднее количество объектов на изображение**: 12


## Класс объекта:
- **1. bicycle**
- **2. motorcycle**
- **3. car**
- **4. transporter (van)**
- **5. bus**
- **6. truck (others)**
- **7. trailer - no instance of it in the dataset**
- **8. unknown**
- **9. mask**


Каждая аннотация связывает объекты с их расположением на изображении и классифицирует их по соответствующему типу.


> [!NOTE]
> Данная аннотация является улучшенной версией стандартной аннотации UA-DETRAC и находится в общем доступе по [ссылке](https://www.kaggle.com/datasets/patrikskalos/ua-detrac-fix-masks-two-wheelers). В стандартной аннотации было только 3 класса.




## Распределение объектов разных классов в датасете в процентом соотношении:
![Gist](https://github.com/irina-krivosheina/AI-24-Team-45/blob/main/images/gist.png?raw=true)
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

## Средний размер (площадь) bbox по классам:
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
