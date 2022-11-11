using System;
using System.Text;
static class Programs
{
    static int[] l1l111l1l1(int l1111l1)
    {
        var l1l1ll1 = new int[l1111l1];
        var last = 0;
        for (int i = 0; i < l1111l1; i++)
        {
            last = ((last * 2 + 35) / 3 + i) % 256;
            l1l1ll1[i] = last ^ i;
        }
        return l1l1ll1;
    }

    static void l1l1l1l11ll(int[] ll1l1l1l1, int[] llll11111)
    {
        for (int i = 0; i < ll1l1l1l1.Length; i++)
        {
            ll1l1l1l1[i] ^= llll11111[i];
        }
    }

    static int[] l11l1l111l(byte[] ll1l1l1l1)
    {
        var output = new int[ll1l1l1l1.Length];
        for (int i = 0; i < ll1l1l1l1.Length; i++)
        {
            output[i] = (int)ll1l1l1l1[i];
        }
        return output;
    }

    static bool ll1l1l1l1l1l1(int[] lllll11111, int[] l1111l111l1)
    {
        for (int i = 0; i < lllll11111.Length; i++)
        {
            if (lllll11111[i] != l1111l111l1[i])
                return false;
        }
        return true;
    }
    static void Main(string[] args)
    {
        Console.WriteLine("Please give me your flag!");
        var lll1l1l1 = Console.ReadLine() ?? throw new Exception("No flag given!");
        var l1l1111l11 = Encoding.UTF8.GetBytes(lll1l1l1);
        var lll1l1l1l = l1l111l1l1(l1l1111l11.Length);
        var l1l11l11l11 = l11l1l111l(l1l1111l11);
        l1l1l1l11ll(l1l11l11l11, lll1l1l1l);
        var l111111111 = new[] { 81, 83, 108, 77, 90, 94, 78, 65, 94, 77, 64, 82, 108, 46, 20, 55, 41, 48, 36, 53, 34, 34, 20, 0, 9, 22, 7, 3, 22, 1, 52, 5, 34, 0, 192, 212, 203, 206, 217, 199, 228, 214, 192, 232, 197, 234, 249, 254, 196, 250, 226, 244, 250, 242 };

        if (ll1l1l1l1l1l1(l111111111, l1l11l11l11))
        {
            Console.WriteLine("TTTTTTTTTTQQQQQQQQQQLLLLLLLLLLLL");
        }
        else
        {
            Console.WriteLine("the flag is moectf{Never_gonna_give_you_up_and_never_gonna_let_you_down}");
        }
    }
}