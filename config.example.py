# GLM Coding Plan 配置文件
# 复制此文件为 config.py 并填入真实值

# ==================== 账号配置 ====================
# 智谱AI登录Cookie（必须）
# 获取方法：登录 bigmodel.cn → F12 → Network → 任意请求复制Cookie头
COOKIE = ""

# ==================== 通知配置 ====================
# 飞书Webhook地址（可选，留空则打印到终端）
FEISHU_WEBHOOK = ""

# 飞书用户ID（可选，用于@某人）
FEISHU_USER_ID = ""

# ==================== 抢购配置 ====================
# 每日抢购时间
GRAB_HOUR = 10
GRAB_MINUTE = 0

# 提前多少秒开始监控（秒）
PRE_START_SECONDS = 30

# 抢购失败后重试间隔（秒）
RETRY_INTERVAL = 1

# 最大重试次数（0=不限制）
MAX_RETRIES = 300

# ==================== 套餐配置 ====================
# 要购买的套餐：lite / pro / max
PLAN_TYPE = "lite"

# 是否自动续订
AUTO_RENEW = True
