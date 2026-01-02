# 三宁职校官网GitHub部署指南

## 一、项目初始化

### 1. 安装Git
确保你的计算机上已经安装了Git。如果没有安装，请访问 [Git官网](https://git-scm.com/) 下载并安装。

### 2. 初始化本地仓库
在项目根目录下执行以下命令：

```bash
git init
```

这将在当前目录创建一个新的Git仓库。

### 3. 配置Git用户信息
```bash
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的GitHub邮箱"
```

## 二、仓库创建

### 1. 在GitHub上创建新仓库
1. 登录你的GitHub账号
2. 点击右上角的 "+" 按钮，选择 "New repository"
3. 填写仓库名称，建议使用 `saning-vocational-school`
4. 选择仓库类型（公开或私有）
5. 不要勾选 "Initialize this repository with a README"（因为我们已经有了README文件）
6. 点击 "Create repository"

### 2. 关联本地仓库与远程仓库
在项目根目录下执行以下命令：

```bash
git remote add origin https://github.com/你的GitHub用户名/saning-vocational-school.git
```

## 三、文件提交

### 1. 添加文件到暂存区
```bash
git add .
```

### 2. 提交文件到本地仓库
```bash
git commit -m "Initial commit: 三宁职校官网项目"
```

### 3. 推送本地仓库到远程仓库
```bash
git push -u origin main
```

## 四、分支管理

### 1. 创建开发分支
```bash
git checkout -b develop
```

### 2. 切换回主分支
```bash
git checkout main
```

### 3. 合并分支
当开发分支的功能完成并测试通过后，可以将其合并到主分支：

```bash
git checkout main
git merge develop
git push origin main
```

### 4. 删除分支
如果不再需要开发分支，可以删除它：

```bash
git branch -d develop  # 删除本地分支
git push origin --delete develop  # 删除远程分支
```

## 五、GitHub Pages配置

### 1. 构建前端项目
在 `frontend` 目录下执行构建命令：

```bash
npm run build
```

### 2. 配置GitHub Pages
1. 登录GitHub，进入你的仓库
2. 点击 "Settings" 选项卡
3. 在左侧菜单中点击 "Pages"
4. 在 "Source" 部分：
   - 选择 "Deploy from a branch"
   - 选择分支：`main`
   - 选择目录：`/frontend/dist`
   - 点击 "Save"

### 3. 等待部署完成
GitHub Pages会自动部署你的网站，通常需要几分钟时间。部署完成后，你可以在 "GitHub Pages" 部分看到你的网站URL。

## 六、常见问题及解决方法

### 1. Git推送失败

**问题**：`git push -u origin main` 失败，提示权限不足。

**解决方法**：
- 确保你有该仓库的推送权限
- 检查你的GitHub凭证是否正确
- 尝试使用SSH方式连接：
  ```bash
  git remote set-url origin git@github.com:你的GitHub用户名/saning-vocational-school.git
  ```

### 2. GitHub Pages部署失败

**问题**：GitHub Pages部署失败，提示构建错误。

**解决方法**：
- 确保你已经正确构建了前端项目
- 检查 `dist` 目录是否存在且包含正确的文件
- 检查GitHub Pages的配置是否正确

### 3. 静态资源加载失败

**问题**：网站部署后，图片等静态资源无法加载。

**解决方法**：
- 检查Vite配置文件中的 `base` 选项是否正确
- 确保静态资源的路径引用正确
- 确保 `index.html` 中的 favicon 等资源使用相对路径
- 当前项目已经正确配置：
  ```javascript
export default defineConfig({
  base: './',
  // 其他配置
})
  ```
- `index.html` 中的 favicon 已经使用相对路径：
  ```html
  <link rel="icon" type="image/svg+xml" href="./vite.svg" />
  ```

### 4. 分支合并冲突

**问题**：合并分支时出现冲突。

**解决方法**：
- 使用文本编辑器手动解决冲突
- 解决冲突后，执行 `git add .` 和 `git commit` 完成合并

### 5. .gitignore文件不生效

**问题**：添加到.gitignore的文件仍然被Git跟踪。

**解决方法**：
- 确保.gitignore文件在项目根目录下
- 确保.gitignore文件的语法正确
- 对于已经被跟踪的文件，可以使用以下命令停止跟踪：
  ```bash
  git rm --cached 文件名
  ```

## 七、持续集成/持续部署（可选）

### 1. 使用GitHub Actions自动部署

创建 `.github/workflows/deploy.yml` 文件，内容如下：

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '18'
    
    - name: Install dependencies
      run: npm install
      working-directory: ./frontend
    
    - name: Build project
      run: npm run build
      working-directory: ./frontend
    
    - name: Deploy to GitHub Pages
      uses: peaceiris/actions-gh-pages@v3
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: ./frontend/dist
```

这样，每次向main分支推送代码时，GitHub Actions都会自动构建并部署你的网站。

## 八、更新网站内容

### 1. 修改代码
在本地修改网站代码。

### 2. 提交修改
```bash
git add .
git commit -m "描述你的修改"
git push origin main
```

### 3. 等待部署
如果配置了GitHub Pages或GitHub Actions，网站会自动更新。

---

以上就是三宁职校官网的GitHub部署指南。如果在部署过程中遇到其他问题，可以参考GitHub的官方文档或在社区寻求帮助。