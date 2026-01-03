# 三宁职校官网

三宁职校官网是一个基于前后端分离架构的现代化职业学校官方网站，提供学校信息展示、课程介绍、师资力量、新闻动态和在线报名等功能。

## 技术栈

### 前端
- **框架**: Vue 3
- **构建工具**: Vite
- **UI组件库**: Element Plus
- **状态管理**: Pinia
- **路由**: Vue Router
- **HTTP客户端**: Axios

### 后端
- **框架**: Flask
- **ORM**: SQLAlchemy
- **认证**: JWT
- **数据库**: MySQL
- **迁移工具**: Flask-Migrate

## 目录结构

```
.
├── .github/          # GitHub配置文件
│   └── workflows/    # GitHub Actions工作流
├── backend/          # 后端代码
│   ├── models/       # 数据模型
│   ├── routes/       # API路由
│   └── app.py        # 应用入口
├── frontend/         # 前端代码
│   ├── public/       # 静态资源
│   ├── src/          # 源代码
│   │   ├── router/   # 路由配置
│   │   ├── store/    # 状态管理
│   │   ├── views/    # 页面组件
│   │   ├── App.vue   # 根组件
│   │   └── main.js   # 入口文件
│   └── package.json  # 前端依赖
└── .gitignore        # Git忽略文件
```

## 快速开始

### 前端部署

1. 进入前端目录
```bash
cd frontend
```

2. 安装依赖
```bash
npm install
```

3. 开发环境运行
```bash
npm run dev
```

4. 生产环境构建
```bash
npm run build
```

5. 预览生产构建
```bash
npm run preview
```

### 后端部署

1. 进入后端目录
```bash
cd backend
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
```bash
cp .env.example .env
# 编辑.env文件，配置数据库连接等信息
```

4. 初始化数据库
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

5. 运行应用
```bash
python app.py
```

## 功能模块

### 1. 首页
- 学校简介
- 最新新闻
- 热门课程
- 优秀师资

### 2. 课程中心
- 课程列表
- 课程详情
- 课程分类

### 3. 师资力量
- 教师列表
- 教师详情
- 教师荣誉

### 4. 新闻动态
- 新闻列表
- 新闻详情
- 新闻分类

### 5. 在线报名
- 报名表单
- 报名状态查询

### 6. 关于我们
- 学校历史
- 校园环境
- 联系我们

### 7. 管理后台
- 用户管理
- 课程管理
- 教师管理
- 新闻管理
- 报名管理

## 贡献指南

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

- 学校官网: [http://www.saning-vocational.com](http://www.saning-vocational.com)
- 邮箱: info@saning-vocational.com
- 电话: 027-88888888

---

**三宁职校官网** © 2026 All Rights Reserved
