# NorthClassVision

ChinaVis 2024数据可视化竞赛作品复现

## 项目简介

本项目是2024年数据可视化竞赛的参赛作品非1:1复现(仅有大致原作成品参考，无原型图、设计稿等)，旨在基于可视化作品学习**D3.js框架**、**前端渲染**与**后端计算**的相关知识。项目主要使用flask、Vue2(包含Vuex)等技术, 还涉及简单的pytest用法。

优化方法目前正在学习, 学习记录、学习资源见**notes**文件夹
各位也可以借助LLM进行询问，自主学习

## 项目结构

项目包含以下核心文件和目录：

```
NorthClassVision/
├── data/
│   ├── Data_SubmitRecord/
│   ├── Data_StudentInfo.csv
│   ├── Data_TitleInfo.csv
│   └── first_dataDes.docx
├── backend/
│   ├── test/
│   │   ├── time_measure.py
│   │   └──mock_data.py
│   ├── utils/
│   │   ├── fs.py
│   │   └── utils.py
│   ├── routes.py
│   └── app.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── router/
│   │   ├── store/
│   │   ├── views/
│   │   └── App.vue
│   ├── .gitignore
│   ├── babel.config.js
│   ├── package.json
│   ├── README.md
│   └── vue.config.js
├── notes/
│   ├── study_recourse.md
│   ├── D3_study.md
│   ├── optimization_journey.md
├── problem.md
└── README.md
```

## 如何运行

0. 参见**problem.md**前往官网下载数据集，放置在data文件夹下

1. 克隆项目到本地：

```bash
git clone https://github.com/holyguacamoleCoder/NorthClassVision.git
```

2. 进入项目目录：

```bash
cd NorthClassVision
```

3. 安装后端依赖：

```bash
pip install -r requirements.txt
```

4. 启动后端服务：

```bash
cd backend
flask run
```

5. 安装前端依赖

```bash
cd ../frontend
npm install
```

6. 启动前端服务：

```bash
cd ../frontend
npm run serve
```

7. 打开浏览器，访问 `http://localhost:8080` 查看可视化效果。

## 样式预览



