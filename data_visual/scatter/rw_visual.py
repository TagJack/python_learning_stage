import matplotlib.pyplot as plt

from random_walk2 import RandomWalk

while True:
    # Построение случайного блуждания и нанесение точек на диаграмму.
    rw = RandomWalk(50000)
    rw_1 = RandomWalk(50000)
    rw_2 = RandomWalk(50000)

    rw.fill_walk()
    rw_1.fill_walk()
    rw_2.fill_walk()
    # Назначение размера области просмотра.
    plt.figure(dpi = 128, figsize=(16, 9))
    # Вывод точек и отображение диаграммы.
    point_number = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Reds, edgecolor='none', s=5)
    plt.scatter(rw_1.x_values, rw_1.y_values, c=point_number, cmap=plt.cm.Blues, edgecolor='none', s=5)
    plt.scatter(rw_2.x_values, rw_2.y_values, c=point_number, cmap=plt.cm.Purples, edgecolor='none', s=5)
    plt.scatter(0, 0, c='green', edgecolor='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)
    # Удаление осей.
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().get_visible(False)
    # plt.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none',s=5)
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if not keep_running == 'y':
        break
#