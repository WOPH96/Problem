e<pair<int, int>> &q)
// {
//     int dx[4] = {1, -1, 0, 0};
//     int dy[4] = {0, 0, 1, -1};
//     int nx, ny;
//     while (!q.empty())
//     {
//         int x, y;
//         x = q.front().first;
//         y = q.front().second;
//         q.pop();
//         for (int i = 0; i < 4; i++)
//         {
//             nx = x + dx[i];
//             ny = y + dy[i];
//             if (0 <= nx && nx < n && 0 <= ny && ny < m && !visited[nx][ny] && graph[nx][ny] != -1)
//             {
//                 if (!graph[nx][ny])
//                 {
//                     visited[nx][ny] = true;
//                     graph[nx][ny] = graph[x][y] + 1;
//                     q.push({nx, ny});
//                 }
//             }
//         }
//     }
// }