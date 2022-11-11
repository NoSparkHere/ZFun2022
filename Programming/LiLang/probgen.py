import random
import string
from http.server import BaseHTTPRequestHandler, HTTPServer

FLAG = "ZFun{wow_you_know_so_much_about_lilang_but_python_is_better_than_it}"


def randstr(length):
    printable = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choices(printable, k=length))


def challenge_gen() -> str:
    randflag = randstr(10) + FLAG + randstr(10)

    part1 = "".join((randflag[i] for i in range(len(randflag)) if i % 3 != 0))
    part2 = "".join((randflag[i] for i in range(len(randflag)) if i % 3 == 0))
    grp = [randstr(random.randint(len(part1) // 2, len(part1) - 1)) for _ in range(9)]
    grp.append(part1)
    random.shuffle(grp)
    grp2 = [randstr(random.randint(len(part2) + 1, len(part2) * 2)) for _ in range(9)]
    grp2.append(part2)
    random.shuffle(grp2)
    return "\n".join(grp + grp2)


class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()

        self.wfile.write(challenge_gen().encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 10006), HTTPHandler)
    print("Server started.")
    server.serve_forever()
