% Trip expenses
index = {'Diane', 'Kelly', 'John'};
columns = {'Food', 'Car', 'Fuel', 'Tickets', 'Other'};
expenses = table(...
    [38.15; 0; 109.75], ... 
    [139; 0; 0], ...
    [25.08; 0; 0], ...
    [0; 134; 0], ...
    [95; 0; 250], ...
    'VariableNames', columns, ...
    'RowNames', index ...
);

% Calculate amount owing
total_paid = sum(expenses{:,:},2);
average_cost = mean(total_paid);
amounts_owing = average_cost - total_paid