# College - 校园助手小程序 (Premium Edition) 🎓

**简体中文** | [English](./README_EN.md) | [日本語](./README_JP.md) | [繁體中文](./README_ZHT.md)

[![Platform](https://img.shields.io/badge/Platform-WeChat%20Mini%20Program-3B82F6?style=for-the-badge&logo=wechat)](https://mp.weixin.qq.com/)
[![Renderer](https://img.shields.io/badge/Renderer-Skyline-8B5CF6?style=for-the-badge)](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)
[![UI Style](https://img.shields.io/badge/UI-Modern%20Glass-F1F5F9?style=for-the-badge)](https://github.com/xuzhentao915/College)

这是一款专为大学生设计的现代化校园助手小程序。项目基于微信最新的 **Skyline 渲染引擎** 开发，采用 **Premium Edition** 标准重构，致力于提供极致的视觉美感与丝滑的交互体验。

## 🌟 核心进化 (New Updates!)

### 1. 智能提醒体系
*   **考试倒计时 (Exam Countdown)**：首页新增玻璃拟态倒计时卡片，自动计算考试剩余天数，并根据紧急程度（≤3天）自动切换**红色预警状态**。
*   **动态公告栏 (Notice Swiper)**：采用 Swiper 轮播设计的玻璃拟态公告位，支持横向滑动，区分“重要/通知”状态标签，信息传递更高效。

### 2. 现代视觉体系 (Visual Design)
*   **玻璃拟态 (Glass-morphism)**：大量运用毛玻璃背景、弥散阴影与动态光斑，营造出通透的层次感。
*   **全线线性图标 (Linear Icons)**：全量采用 3px 笔触的线性简约风格图标，视觉高度统一。

### 3. Skyline 交互优化
*   **区域滚动方案**：针对 Skyline 引擎深度定制的 `scroll-view` 布局，实现了“成绩单局部滚动”与“首页全量顺滑滚动”，完美平衡固定看板与长列表内容。
*   **智能导航适配**：自研 `navigation-bar` 组件，动态适配 iOS/Android 全机型状态栏。

## 📸 模块概览

- **首页 (Home)**：智能时段问候、考试压力提醒、动态轮播公告、今日课程看板。
- **课表 (Schedule)**：动态时间轴布局，支持按星期筛选，自动定位今日行程。
- **成绩 (Grade)**：GPA 视觉仪表盘，支持学期切换，成绩单智能着色管理。
- **我的 (User)**：悬浮个人名片，全图标化分类功能菜单。

## 🛠️ 技术细节

- **渲染引擎**: Skyline (Glass-Easel 组件框架)
- **图标引擎**: `scripts/gen_icons.py` (Python 算法生成全套线性 PNG 图标)
- **适配方案**: 动态计算 `navHeight` 与 `safeAreaBottom`

## 🚀 快速开始

1. **克隆项目**:
   ```bash
   git clone https://github.com/xuzhentao915/College.git
   ```
2. **导入开发者工具**:
   - 选择“导入项目”，目录指向 `College` 文件夹。
   - 确保 **“使用 Skyline 渲染引擎”** 已勾选。

---
*Developed with Modern Standards by xuzhentao915*
