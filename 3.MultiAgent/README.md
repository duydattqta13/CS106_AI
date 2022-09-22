# HW3
+ Tự tương tác điều khiển: python pacman.py
+ Tự tương tác điều khiển với một file layout tùy chọn (sử dụng thêm -l flag): ví dụ python pacman.py -l trickyClassic
+ Yêu câu chạy một thuật toán nào đó (sử dụng -p flag): ví dụ python pacman.py -l mediumClassic -p ExpectimaxAgent
+ Yêu cầu chạy một thuật toán nào đó với số tầng mong muốn trong game tree (số bước nhìn trước), ví dụ: python pacman.py -l mediumClassic -p MinimaxAgent -a depth=3
+ Yêu cầu chạy một thuật toán nào đó với số tầng mong muốn  trong game tree (số bước nhìn trước) và sử dụng một hàm lượng giá nào đó, ví dụ: python pacman.py -l mediumClassic -p MinimaxAgent -a depth=3,evalFn=betterEvaluationFunction
+ Mỗi lần chạy chương trình sẽ dùng một random seed khác nhau. Có thể cố định random seed cho dễ debug bằng cách dùng -f flag. Ví dụ python pacman.py -l mediumClassic -p MinimaxAgent -a depth=3,evalFn=betterEvaluationFunction -f 
+ Có thể sử dụng thêm option --frameTime 0 để rút ngắn thời gian simulation.
+ Có thể tham khảo thêm cách sử dụng chi tiết ở đây: https://inst.eecs.berkeley.edu/~cs188/fa19/project2/