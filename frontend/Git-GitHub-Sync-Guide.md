# Git 同步到 GitHub 完整指南

## 一、准备工作

### 1. 确认本地仓库状态
首先检查当前仓库状态，确认本地仓库与远程仓库的关联情况：

```bash
git status
```

### 2. 确认远程仓库关联
检查本地仓库是否已关联远程仓库：

```bash
git remote -v
```

**结果说明**：
- 若显示类似 `origin  https://github.com/用户名/仓库名.git (fetch/push)`，则说明已关联远程仓库
- 若未关联，可通过以下命令关联：
  ```bash
  git remote add origin https://github.com/用户名/仓库名.git
  ```

## 二、检查文件修改状态

使用 `git status` 命令查看已修改的文件：

```bash
git status
```

**输出说明**：
- `Changes not staged for commit`: 已修改但未暂存的文件
- `Untracked files`: 未被Git跟踪的新文件

## 三、暂存更改

### 1. 暂存单个文件
```bash
git add 文件名
```

### 2. 暂存所有修改文件
```bash
git add .
```

### 3. 选择性暂存
```bash
git add -p  # 交互式选择要暂存的修改
```

## 四、提交更改

### 1. 基本提交命令
```bash
git commit -m "提交信息"
```

### 2. 规范的提交信息格式
推荐使用以下格式：

```
<类型>: <简短描述>

<详细描述（可选）>

<关联的Issue或任务（可选）>
```

**类型说明**：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档修改
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建或依赖更新

**示例**：
```bash
git commit -m "fix: 修复教师页面图片显示问题

修改了TeachersView.vue中的图片路径配置，解决图片加载失败问题

关联Issue: #123"
```

## 五、推送到远程GitHub仓库

### 1. 推送当前分支
```bash
git push origin 分支名
```

### 2. 设置上游分支（首次推送）
```bash
git push -u origin 分支名
```

### 3. 强制推送（谨慎使用）
```bash
git push -f origin 分支名
```

## 六、常见问题及解决方法

### 1. 本地仓库与远程仓库冲突
**问题**：推送时提示 `error: failed to push some refs to 'https://github.com/...'`

**解决方法**：
```bash
# 先拉取远程仓库的最新代码
git pull origin 分支名
# 解决冲突后重新提交并推送
git add .
git commit -m "解决冲突"
git push origin 分支名
```

### 2. 忘记关联远程仓库
**问题**：推送时提示 `fatal: 'origin' does not appear to be a git repository`

**解决方法**：
```bash
git remote add origin https://github.com/用户名/仓库名.git
git push -u origin 分支名
```

### 3. 提交信息写错
**问题**：提交后发现提交信息有误

**解决方法**：
```bash
# 修改最后一次提交信息
git commit --amend -m "新的提交信息"
# 强制推送到远程
git push -f origin 分支名
```

### 4. 暂存了错误的文件
**问题**：不小心暂存了不需要提交的文件

**解决方法**：
```bash
# 取消单个文件的暂存
git reset HEAD 文件名
# 取消所有文件的暂存
git reset HEAD
```

## 七、完整操作示例

假设我们修改了 `src/views/TeachersView.vue` 文件，完整的同步流程如下：

1. **检查修改状态**：
   ```bash
git status
   ```

2. **暂存修改**：
   ```bash
git add src/views/TeachersView.vue
   ```

3. **提交修改**：
   ```bash
git commit -m "feat: 更新教师页面图片显示样式

调整了教师列表的图片布局和样式，提升页面美观度"
   ```

4. **推送到远程**：
   ```bash
git push origin master
   ```

## 八、图形界面工具推荐

如果不习惯命令行，可使用以下图形界面工具：

1. **GitHub Desktop**：官方推荐，简单易用
2. **GitKraken**：功能强大，界面友好
3. **VS Code 内置 Git**：直接在编辑器中操作，适合开发场景

## 九、注意事项

1. **定期拉取**：在开始工作前，先执行 `git pull` 获取最新代码
2. **小步提交**：尽量将大的修改拆分为多个小的、有意义的提交
3. **规范提交信息**：使用清晰、规范的提交信息，便于后续维护和查找
4. **保护主分支**：建议在开发分支上工作，完成后通过Pull Request合并到主分支
5. **忽略不必要的文件**：使用 `.gitignore` 文件排除不需要跟踪的文件（如node_modules、build等）

## 十、常用Git命令速查

| 命令 | 功能描述 |
|------|----------|
| `git status` | 查看仓库状态 |
| `git add .` | 暂存所有修改 |
| `git commit -m "信息"` | 提交修改 |
| `git push origin 分支` | 推送到远程分支 |
| `git pull origin 分支` | 从远程拉取代码 |
| `git branch` | 查看本地分支 |
| `git branch -a` | 查看所有分支（本地+远程） |
| `git checkout 分支` | 切换分支 |
| `git merge 分支` | 合并分支 |
| `git log` | 查看提交历史 |

---

**更新日期**：2026-01-03
**适用场景**：前端项目Git管理，Vue项目部署
**作者**：AI Assistant