using System;
using System.Text;
static class Programs
{
    static int[] func(int length)
    {
        var array = new int[length];
        var last = 0;
        for (int i = 0; i < length; i++)
        {
            last = ((last * 2 + 35) / 3 + i) % 256;
            array[i] = last ^ i;
        }
        return array;
    }

    static void strxor(int[] buffer, int[] buffer2)
    {
        for (int i = 0; i < buffer.Length; i++)
        {
            buffer[i] ^= buffer2[i];
        }
    }

    static int[] copydata(byte[] buffer)
    {
        var output = new int[buffer.Length];
        for (int i = 0; i < buffer.Length; i++)
        {
            output[i] = (int)buffer[i];
        }
        return output;
    }

    static bool checkFlag(int[] array1, int[] array2)
    {
        for (int i = 0; i < array1.Length; i++)
        {
            if (array1[i] != array2[i])
                return false;
        }
        return true;
    }
    static void Main(string[] args)
    {
        Console.WriteLine("Please give me your flag!");
        var input = Console.ReadLine() ?? throw new Exception("No flag given!");
        var encoded = Encoding.UTF8.GetBytes(input);
        var encoded2 = func(encoded.Length);
        var data2 = copydata(encoded);
        strxor(data2, encoded2);
        var data = new[] { 81, 83, 108, 77, 90, 94, 78, 65, 94, 77, 64, 82, 108, 46, 20, 55, 41, 48, 36, 53, 34, 34, 20, 0, 9, 22, 7, 3, 22, 1, 52, 5, 34, 0, 192, 212, 203, 206, 217, 199, 228, 214, 192, 232, 197, 234, 249, 254, 196, 250, 226, 244, 250, 242 };

        if (checkFlag(data, data2))
        {
            Console.WriteLine("TTTTTTTTTTQQQQQQQQQQLLLLLLLLLLLL");
        }
        else
        {
            Console.WriteLine("the flag is moectf{Never_gonna_give_you_up_and_never_gonna_let_you_down}");
        }
    }
}