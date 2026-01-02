# GitHub Pages部署修复方案

## 问题分析
GitHub Actions部署失败，静态资源无法访问，返回404错误。

## 修复步骤

### 1. 登录GitHub账户
访问 https://github.com/toney17951-123456/saning-vocational-school

### 2. 配置GitHub Pages
1. 点击仓库页面顶部的 "Settings" 选项卡
2. 在左侧菜单中点击 "Pages"
3. 在 "Source" 部分：
   - 选择 "Deploy from a branch"
   - 选择分支：`master`
   - 选择目录：`/frontend/dist`
   - 点击 "Save"

### 3. 等待部署完成
GitHub Pages会自动部署你的网站，通常需要几分钟时间。部署完成后，你可以在 "GitHub Pages" 部分看到你的网站URL。

## 替代方案：手动部署

如果GitHub Pages自动部署仍有问题，你可以使用以下命令手动部署：

```bash
# 安装gh-pages工具
npm install -g gh-pages

# 切换到frontend目录
cd frontend

# 部署到gh-pages分支
gh-pages -d dist -r https://github.com/toney17951-123456/saning-vocational-school.git
```

## 验证部署
部署完成后，访问以下URL验证网站是否正常工作：
https://toney17951-123456.github.io/saning-vocational-school/