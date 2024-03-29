import requests
from bs4 import BeautifulSoup

def parse_title(url, soup):
    if "jmir.org" in url:
        return soup.find('h1').get_text().strip()
    # 添加其他网站的解析规则
    else:
        return soup.find('title').get_text().strip() if soup.find('title') else "标题未找到"

def get_user_agent(device_type):
    user_agents = {
        'desktop': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'mobile': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }
    return user_agents.get(device_type, user_agents['desktop'])

# URLs列表
urls = [
    "https://formative.jmir.org/2024/1/e50056",
    "https://www.proquest.com/openview/1dccdeab218b1ac51ca7ef049c3c6636/1?pq-origsite=gscholar&cbl=18750&diss=y"
    "https://link.springer.com/article/10.1007/s10994-023-06460-4"
    "https://ieeexplore.ieee.org/abstract/document/10392451"
    "https://ieeexplore.ieee.org/abstract/document/10132404"
    "https://eprints.whiterose.ac.uk/209218/"
    "https://ieeexplore.ieee.org/abstract/document/10373072"
    "https://dl.acm.org/doi/abs/10.1145/3583133.3590703"
    "https://www.emerald.com/insight/content/doi/10.1108/IR-11-2023-0284/full/html"
    "https://dl.acm.org/doi/abs/10.1145/3581783.3613965"
    "https://www.mdpi.com/2079-9292/12/4/970"
    "https://arxiv.org/abs/2312.12255"
    "https://ieeexplore.ieee.org/abstract/document/10207979"
    "https://arxiv.org/abs/2308.10721"
    "https://arxiv.org/abs/2401.12258"
    "https://dl.acm.org/doi/full/10.1145/3585276"
    "https://dl.acm.org/doi/abs/10.5555/3545946.3598702"
    "https://proceedings.neurips.cc/paper_files/paper/2023/hash/b048dd19ba6d85b9066aa93b4de9ad4a-Abstract-Conference.html"
    "https://link.springer.com/article/10.1007/s11721-024-00235-w"
    "https://ieeexplore.ieee.org/abstract/document/10123696"
    "https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/cps2.12065"
    "https://arxiv.org/abs/2301.03398"
    "https://www-users.cse.umn.edu/~gini/publications/papers/Sylvester-arms23.pdf"
    "https://www.sciencedirect.com/science/article/abs/pii/S0305054823001582"
    "https://www.mdpi.com/2071-1050/15/24/16741"
    "https://www.chkwon.net/papers/park_learn.pdf"
    "https://www.mdpi.com/2076-3417/13/16/9174"
    "https://link.springer.com/article/10.1007/s10489-022-04426-y"
    "https://formative.jmir.org/2024/1/e50056"
    "https://ieeexplore.ieee.org/abstract/document/10356649"
    "https://www.sciencedirect.com/science/article/abs/pii/S0264410X23010162"
    "https://openurl.ebsco.com/EPDB%3Agcd%3A11%3A22139275/detailv2?sid=ebsco%3Aplink%3Ascholar&id=ebsco%3Agcd%3A173381058&crl=c"
    "https://www.sciencedirect.com/science/article/abs/pii/S1474034623000861"
    "https://journals.sagepub.com/doi/full/10.1177/00375497231184898"
    "https://www.sciencedirect.com/science/article/abs/pii/S0921889023000817"
    "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4343647"
    "https://www.tandfonline.com/doi/abs/10.1080/17477778.2022.2080008"
    "https://dl.acm.org/doi/abs/10.1145/3585088.3589357"
    "https://iwaponline.com/jh/article/25/3/912/94555/Artificial-intelligence-for-decentralized-water"
    "https://link.springer.com/article/10.1007/s40747-022-00780-z"
    "https://arxiv.org/abs/2403.01600"
    "https://www.mdpi.com/2079-8954/11/3/130"
    "https://www.sciencedirect.com/science/article/abs/pii/S0198971523000832"
    "https://www.ifaamas.org/Proceedings/aamas2023/pdfs/p2730.pdf"
    # 其他链接
]

device_type = 'desktop'  # 或 'mobile'
headers = {'User-Agent': get_user_agent(device_type)}

for url in urls:
    try:
        print(f"url: {url}")
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = parse_title(url, soup)
        print(title)
    except Exception as e:
        print(f"无法从 {url} 爬取数据: {e}")

