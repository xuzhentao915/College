# College - 校园助手小程序 🎓

[![Platform](https://img.shields.io/badge/Platform-WeChat%20Mini%20Program-5B8CFF?style=flat-square&logo=wechat)](https://mp.weixin.qq.com/)
[![Renderer](https://img.shields.io/badge/Renderer-Skyline-764BA2?style=flat-square)](https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html)
[![Style](https://img.shields.io/badge/Style-Neu--morphism-E4EAF0?style=flat-square)](https://github.com/Mortal915/College)

这是一款专为大学生打造的轻量级校园助手小程序。采用微信最新的 **Skyline 渲染引擎** 开发，拥有极致的流畅度与现代化的**新拟态 (Neu-morphism)** 视觉设计。

## ✨ 项目亮点

*   🚀 **高性能渲染**：全面启用 Skyline 渲染引擎，支持更复杂的动画与手势交互。
*   🎨 **精致视觉**：深度定制的新拟态 UI 体系，柔和的光影质感，极具现代感。
*   📊 **数据看板**：
    *   **今日课表**：智能提醒当日课程及教室。
    *   **GPA 管理**：自动计算学期绩点，成绩分布一目了然。
*   🛠️ **极客工具**：内置 Python 脚本算法生成 TabBar 图标，追求零资源浪费。

## 📸 功能模块

- **首页 (Home)**: 实时时间问候、功能快捷入口、今日课程概览、校园通知。
- **课表 (Schedule)**: 交互式周课表，支持日期自动切换，清晰的时间轴布局。
- **成绩 (Grade)**: 历史成绩查询、GPA 仪表盘、成绩自动着色（优良及格识别）。
- **我的 (User)**: 个人信息展示、功能菜单导航。

## 🛠️ 技术细节

- **渲染引擎**: Skyline (Glass-Easel 组件框架)
- **样式变量**: 全局 CSS 变量控制，支持秒级换肤。
- **图标方案**: `scripts/gen_icons.py` (Python 算法生成) + SVG Data URI。

## 🚀 快速开始

1. **克隆项目**:
   ```bash
   git clone https://github.com/Mortal915/College.git
   ```
2. **导入开发者工具**:
   - 打开“微信开发者工具”。
   - 选择“导入项目”，目录指向 `College` 文件夹。
   - 确保 `project.config.json` 中的 `renderer` 为 `skyline`。

## 📄 开源协议
[MIT License](LICENSE)

---
*Created with ❤️ by Mortal915*
