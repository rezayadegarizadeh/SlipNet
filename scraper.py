import re
import requests
import time
from datetime import datetime, timedelta
from collections import OrderedDict
from zoneinfo import ZoneInfo

# ========== CONFIGURATION ==========
TEHRAN_TZ = ZoneInfo("Asia/Tehran")

CHANNELS = [
    "xgvpn",
    "appxa",
    "appxa2",
    "IRNOTPHONE",
    "IRAN_V2RAY1",
    "SlipNet_decode",
    "blackRay",
    "SparrK_VPN",
    "slipnet_chat",
    "SlipNet_app",
    "VConfing",
    "capcutchina",
    "v2ray_configs_pool",
    "ep_not",
    "oonfig",
    "config_hatunnel",
    "FreakConfig",
    "Prossh",
    "Express_freevpn",
    "AirdropKhas",
    "NetAccount",
    "internet_tol",
    "asrnovin_ir",
    "deamnet",
    "vip_fragment_v2ray",
    "Clockwise_Groove",
    "bugfreenet",
    "MTProto_Proxyes",
    "proxyvpn11",
    "ServerNett",
    "anty_filter",
    "hamester_109",
    "iphone02016vpn",
    "tanhanet",
    "SoftNET",
    "myandroidplus",
    "Marambashi",
    "WBnet",
    "wiski",
    "sosiran",
    "vpnbaz",
    "SOSIranConnect04",
    "n2vpn",
    "jojo",
    "nikaSS",
    "JavidnamanIran",
    "salad",
    "number1",
    "rostam",
    "FreeIR",
    "WallWeb",
    "Telegram_WallWeb",
    "TelegramWallWeb",
    "Wall_Web",
    "SOSIranConnect05",
    "filterchi",
    "mahsa",
    "mmahsa",
    "break_the_barriers",
    "breakthebarriers",
    "Tirexnet",
    "filterchi03",
    "spark",
    "Dozdi-nakon-nisharaf-20",
    "Dozdi-nakon-nisharaf",
    "WallWebTelegram",
    "WallWeb_Telegram",
    "zel2ovpn",
    "vpnir404",
    "vpn_ir_404",
    "vpn_ir404",
    "vpnir_404",
    "iampedi",
    "whitedns",
    "wiki_tajrobe",
    "vpnsshocean",
    "2475571063-rojproxy",
    "rojproxy",
    "v2rayngvpn",
    "SabzNetBot",
    "sabznetvpn",
    "vpn_Click",
    "proxymtprotoir",
    "VPNSabzSeller",
    "givevpn",
    "rom1_ir",
    "FreeVPNShield",
    "niazcom_ir",
    "linkdoni_irtele",
    "wireguard_w",
    "shit_mamad",
    "HotNudss",
    "networkvppn",
    "Vpn_Shield_Gp",
    "configv2rayng",
    "v2configer",
    "nemigam",
    "bamak",
    "v2rayrun",
    "v2rayrun0",
    "v2raytun",
    "v2raytun0",
    "AirdropKhas",
    "pingkhorbot",
    "pingkhor_cha",
    "BefarmaLink",
    "apkclub",
    "red_server_ips",
    "V2ray_official",
    "WallWeb-noizdns",
    "WallWebnoizdns",
    "WallWeb_noizdns",
    "viinews",
    "vlinews",
    "swagmeli",
    "parsashonam",
    "Telegram.Parsashonam",
    "TelegramParsashonam",
    "Telegram-Parsashonam",
    "Telegram_Parsashonam",
    "v2dogs",
    "v2dogs_n",
    "Clockwise_Groove",
    "Clockwise",
    "Groove",
    "tweetycp",
    "mysubcake",
    "myiranbanoo",
    "adnanpes",
    "v2rayng0201",
    "v2rayng020",
    "v2rayng02",
    "v2rayng0",
    "v2rayng",
    "yazi2",
    "yazi",
    "amir_webstudio",
    "masterdnsvpn",
    "cryptookade",
    "xixv2ray",
    "EfixVPN",
    "maxilium",
    "ghalagyann2",
    "configprxy",
    "netpluss_vpn",
    "config_ng",
    "kanfing_proxy1",
    "kanfing_proxy",
    "eshgheabadii_facts",
    "vasl_bashim",
    "proxylabra",
    "vpn_freeconfiglab",
    "d1eghbali",
    "iiproxyIran",
    "velx",
    "mr_seed4me1",
    "masoud_v2ray",
    "pakhshekhayam",
    "total_fut",
    "safeport_vpn",
    "iphone02016vpn",
    "god_internet1",
    "config_ng",
    "Pirimod",
    "turkishmusicdl",
    "Mr_Filtershekan",
    "computer_quchan",
    "filterban",
    "hyper_vpn",
    "filtershekan_channel",
    "World_Filtershekan",
    "VPN_Moorche",
    "nthlink",
    "AzadNet",
    "tasiyanc",
    "filtershekanpro",
    "omidiranazad",
    "kamkarstore",
    "sinavm",
    "SiNA_TEC",
    "tg207547377_nnjgoqm7",
    "nnjgoqm7",
    "tg207547377",
    "tg207547377nnjgoqm7",
    "tg_nnjgoqm7",
    "tgnnjgoqm7",
    "freedom",
    "decrypt",
    "freedomdecrypt",
    "freedom_decrypt",
    "suturnvpn1",
    "iranux",
    "socksproxy",
    "tg576916081_xad6dr9k",
    "ai_duet",
    "tanhanet",
    "sosiranconnect",
    "FreeInternetForJojo",
    "SlipGate_hub",
    "WebPackClub",
    "azadi_az_inja_migzare",
    "persianvpnhub"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

SLIPNET_REGEX = re.compile(r'slipnet(?:-enc)?:\/\/[^\s<>"\'\[\]{}|\\^`]+', re.IGNORECASE)

OUTPUT_FILE = "☬SHΞN™.txt"

# ========== FUNCTIONS ==========
def fetch_channel_page(username: str) -> str:
    url = f"https://t.me/s/{username}"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"[!] Error fetching {username}: {e}")
        return ""

def extract_links_from_html(html: str) -> set:
    return set(SLIPNET_REGEX.findall(html))

def get_next_refresh(minutes=10) -> str:
    """زمان بعدی به‌روزرسانی با وقت تهران (بر اساس cron 10 دقیقه)"""
    now_tehran = datetime.now(TEHRAN_TZ)
    future = now_tehran + timedelta(minutes=minutes)
    return future.strftime("%I:%M %p").lstrip("0")

def generate_output(per_channel_data: OrderedDict, total_unique: int) -> str:
    now_tehran = datetime.now(TEHRAN_TZ)
    now_str = now_tehran.strftime("%Y-%m-%d %H:%M:%S")
    next_refresh = get_next_refresh(10)  # 10 دقیقه بعد

    lines = []
    lines.append("☬Exclusive SHΞN™ made")
    lines.append("Live SlipNet Node Collector")
    lines.append(f"Last update: {now_str}      Total node : {total_unique}   Next refresh: {next_refresh}")
    lines.append("")  # خط خالی قبل از اولین بخش

    for ch, links in per_channel_data.items():
        count = len(links)
        if count == 0:
            continue
        lines.append(f"Slipnet nod from : {ch} {count} Node")
        lines.append("")  # خط خالی بعد از عنوان
        # هر کانفیگ در یک خط مجزا (بدون کاراکتر اضافی)
        for link in links:
            lines.append(link)
        lines.append("")  # خط خالی بین سورس‌ها

    # ========== فوتر جدید با آرت ASCII ==========
    lines.append("Overhauld ☬ SHΞЯVIN™")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⢀⣤⣾⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠉⠀⠀⠚⠛⠛⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⠉⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⠤⠀⠉⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠉⠉⢀⣀⣤⣶⣾⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠒⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⣶⣶⠀⢰⣶⣶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⡀⠙⠋⢀⡀⠈⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠿⣶⡶⠿⣿⣿⠶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⣿⡇⠀⣿⣿⠀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠀⣿⣇⣀⣿⣿⠀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠛⠛⠛⠛⠛⠛⠛⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣶⣶⣶⠀⣶⣶⣶⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠿⠿⠿⠀⠿⠿⠿⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⠋⢀⣿⠋⢀⡀⠙⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣇⠀⢿⡏⢀⣾⡿⠀⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣤⣀⣀⣼⣇⣀⣰⣿⣿⣿⣿⣿")
    lines.append("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    lines.append("☬Exclusive SHΞN™ made")
    lines.append("More !? T.me/Shervini")

    return "\n".join(lines)

def main():
    print(f"[{datetime.now(TEHRAN_TZ).isoformat()}] Starting SlipNet collector (TXT mode)")

    per_channel_links = OrderedDict()
    all_unique_links = set()

    for ch in CHANNELS:
        print(f"  -> Fetching {ch}")
        html = fetch_channel_page(ch)
        if not html:
            per_channel_links[ch] = []
            continue

        links = extract_links_from_html(html)
        if not links:
            per_channel_links[ch] = []
            print(f"      No slipnet links found")
        else:
            unique_links = list(links)
            per_channel_links[ch] = unique_links
            all_unique_links.update(unique_links)
            print(f"      Found {len(unique_links)} unique slipnet link(s)")

        time.sleep(1)  # احترام به محدودیت

    total_unique_all = len(all_unique_links)
    print(f"Total unique configs (across all channels): {total_unique_all}")

    # بازنویسی کامل فایل (حتی اگر لینک‌ها تغییر نکرده باشند، timestamp ها عوض می‌شوند)
    output_content = generate_output(per_channel_links, total_unique_all)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(output_content)

    print(f"✅ Output saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
