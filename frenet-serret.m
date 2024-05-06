function frenet_serret()

    % 定义曲线上每段的曲率和挠率
    curvatures = [1, 1, 1, 5, 1, 1, 1, 1,5];  % 曲率列表
    torsions = [0.1, 0.1, 0.1, -0.1, 0, 0, 0, 0,0.2];  % 挠率列表

    % 初始化曲线的初始点和切线、法线和次法线
    start_point = [0, 0, 0];
    start_TNB = {[1, 0, 0], [0, 1, 0], [0, 0, 1]};

    % 分段计算曲线的Frenet-Serret框架
    curve_points_all = [start_point];
    for i = 1:length(curvatures)
        [curve_points, start_TNB] = compute_curve_segment(curvatures(i), torsions(i), curve_points_all(end,:), start_TNB);
        curve_points_all = [curve_points_all; curve_points(2:end,:)];
    end

    % 绘制曲线路径
    figure;
    plot3(curve_points_all(:,1), curve_points_all(:,2), curve_points_all(:,3), 'b');
    xlabel('X');
    ylabel('Y');
    zlabel('Z');
    title('Curve Path');
    grid on;

end

function [curve_points, new_TNB] = compute_curve_segment(curvature, torsion, start_point, start_TNB)

    num_points = 100;
    dt = 1 / num_points;

    T = start_TNB{1};
    N = start_TNB{2};
    B = start_TNB{3};

    curve_points = zeros(num_points, 3);
    curve_points(1,:) = start_point;

    for i = 2:num_points
        T = T + curvature * N * dt;
        N = N + (torsion * B - curvature * T) * dt;
        B = B - torsion * N * dt;
        curve_points(i,:) = curve_points(i-1,:) + T * dt;
    end

    new_TNB = {T, N, B};

end
