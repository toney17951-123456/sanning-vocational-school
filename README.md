# 三宁职业技术学校官网

![GitHub license](https://img.shields.io/github/license/yourusername/sanning-vocational-school)
![GitHub stars](https://img.shields.io/github/stars/yourusername/sanning-vocational-school?style=social)
![GitHub forks](https://img.shields.io/github/forks/yourusername/sanning-vocational-school?style=social)

## 🏫 项目简介

三宁职业技术学校官网是一个专为职校宣传和业务课程推广设计的现代化响应式网站。网站以展示学校实力、宣传特色课程、吸引学员报名为核心目标，采用简洁大气的设计风格，突出职校教育特色和专业课程优势。

## 🎯 核心功能

### 📖 职校宣传模块
- **学校概况**：展示学校历史、办学理念、硬件设施
- **师资力量**：详细介绍优秀教师团队，突出专业背景和教学经验
- **校园环境**：通过图片和文字呈现现代化校园设施
- **办学成果**：展示学员就业率、合作企业、荣誉资质

### 📚 业务课程推广
- **课程分类**：清晰展示各类职业技能培训课程
- **课程详情**：包含课程大纲、授课方式、学习周期、就业方向
- **名师授课**：突出名师教学优势，增强课程吸引力
- **在线咨询**：便捷的课程咨询通道

### 📝 在线报名系统
- **课程报名**：支持多种课程在线报名
- **信息采集**：完整的学员信息收集表单
- **支付功能**：支持微信、支付宝等多种支付方式

### 📰 新闻动态
- **学校新闻**：发布学校最新活动和通知
- **行业资讯**：分享相关行业最新动态和发展趋势

## 💻 技术栈

### 前端
- Vue 3 + Vite - 现代化前端框架，构建快速响应的用户界面
- Element Plus - 企业级UI组件库，提供丰富的交互组件
- Vue Router - 前端路由管理
- SCSS - 强大的CSS预处理器，实现优雅的样式设计

### 后端
- Python Flask - 轻量级Web框架，处理API请求
- SQLAlchemy - ORM框架，简化数据库操作
- JWT - 安全的身份验证机制
- MySQL 8.0 - 稳定可靠的关系型数据库

## 🚀 快速开始

### 本地运行

#### 前端
```bash
cd frontend
npm install
npm run dev
```

#### 后端
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # 配置环境变量
python app.py
```

### 访问方式
- 前端访问：http://localhost:5173
- 后端API：http://localhost:5000

## 📁 项目结构

```
├── frontend/           # 前端项目
│   ├── src/            # 前端源代码
│   │   ├── views/      # 页面组件
│   │   │   ├── HomeView.vue       # 首页
│   │   │   ├── AboutView.vue      # 学校简介
│   │   │   ├── TeachersView.vue   # 师资介绍
│   │   │   ├── CoursesView.vue    # 课程展示
│   │   │   ├── NewsView.vue       # 新闻中心
│   │   │   └── ApplyView.vue      # 在线报名
│   │   ├── App.vue     # 根组件
│   │   └── main.js     # 入口文件
│   ├── public/         # 静态资源（图片、视频等）
│   └── package.json    # 前端依赖配置
├── backend/            # 后端项目
│   ├── models/         # 数据库模型
│   ├── routes/         # API路由
│   ├── app.py          # 后端入口
│   └── requirements.txt # 后端依赖
├── README.md           # 项目说明文档
└── .trae/              # Trae AI配置
```

## 🎨 设计特点

1. **响应式设计**：适配各种屏幕尺寸，从手机到桌面设备
2. **现代化UI**：采用简洁大气的设计风格，突出内容重点
3. **优化的用户体验**：清晰的导航结构，便捷的操作流程
4. **课程导向**：以课程为核心，突出课程优势和就业前景
5. **视觉吸引力**：高质量图片和合理的排版布局

## 🔧 定制与扩展

### 修改课程信息
- 课程数据位于 `frontend/src/views/CoursesView.vue`
- 可通过修改组件内的课程数组或连接后端数据库动态获取

### 更新师资信息
- 教师数据位于 `frontend/src/views/TeachersView.vue`
- 支持添加教师头像、简介、擅长课程等信息

### 替换校园图片
- 图片资源存放在 `frontend/public/images/` 目录
- 可根据需要替换或添加新图片

### 修改导航菜单
- 导航配置位于 `frontend/src/router/index.js`
- 可添加、删除或修改导航栏目

## 🌐 部署到GitHub Pages

### 前端部署
```bash
cd frontend
npm install
npm run build
```

1. 确保 `vite.config.js` 中配置了正确的 `base` 路径
2. 将 `dist` 目录推送到GitHub仓库
3. 在GitHub仓库设置中启用GitHub Pages，选择 `dist` 目录

### 后端部署
后端推荐部署到云服务平台：
- Heroku
- Render
- Vercel
- AWS Elastic Beanstalk

## 📋 课程管理

### 课程信息格式
```javascript
{
  id: 1,
  title: '课程名称',
  category: '课程分类',
  teacher: '授课教师',
  duration: '学习时长',
  price: '课程价格',
  description: '课程简介',
  content: '课程详细内容',
  start_time: '开始时间',
  end_time: '结束时间',
  image: '课程图片路径'
}
```

### 新增课程流程
1. 准备课程相关资料（名称、简介、大纲、图片等）
2. 在对应组件中添加课程数据或通过后台管理系统添加
3. 确保课程分类和标签设置合理
4. 测试课程展示效果

## 👨‍🏫 师资管理

### 教师信息格式
```javascript
{
  id: 1,
  name: '教师姓名',
  title: '教师职称',
  department: '所属部门',
  avatar: '教师头像',
  bio: '教师简介',
  expertise: '擅长领域',
  courses: ['讲授课程1', '讲授课程2']
}
```

## 📊 网站数据分析

建议集成以下分析工具，了解网站访问情况：
- **百度统计**：国内常用的网站统计工具
- **Google Analytics**：全球领先的数据分析平台
- **CNZZ**：简单易用的网站流量统计

## 🤝 贡献指南

欢迎对本项目进行贡献！以下是贡献的基本流程：

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 打开 Pull Request

## 📝 提交规范

请遵循以下提交信息规范：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码风格调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建或工具相关

## � 安全注意事项

在将项目部署到生产环境之前，请务必注意以下安全配置：

1. **环境变量安全**
   - 不要将 `.env` 文件提交到 GitHub（已在 `.gitignore` 中配置）
   - 生产环境中使用强随机生成的 `SECRET_KEY` 和 `JWT_SECRET_KEY`
   - 定期更换密钥和密码

2. **数据库安全**
   - 生产环境中不要使用 `root` 用户连接数据库
   - 创建专用数据库用户，只授予必要的权限
   - 使用强密码保护数据库

3. **支付配置安全**
   - 微信支付和支付宝的密钥信息必须妥善保管
   - 生产环境中使用真实的支付配置，开发环境使用沙箱环境

4. **服务器配置**
   - 生产环境中设置 `FLASK_ENV=production` 和 `FLASK_DEBUG=False`
   - 配置合适的 CORS 策略，只允许必要的域名访问
   - 使用 HTTPS 协议，配置 SSL 证书

5. **依赖安全**
   - 定期更新依赖包，修复已知漏洞
   - 使用 `pip audit` 或 `npm audit` 检查依赖包安全性

## �📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 📞 联系方式

- 学校地址：[请填写学校地址]
- 联系电话：[请填写联系电话]
- 电子邮箱：[请填写电子邮箱]
- 官方网站：[请填写官方网站地址]

## 🙏 致谢

感谢所有为本项目做出贡献的开发者！

---

**三宁职业技术学校** - 培养技能人才，助力职业发展

✨ 感谢您对三宁职校的关注与支持！