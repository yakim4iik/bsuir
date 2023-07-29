#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

void static vvod(int* strlength, int** list, int amount) // ввод списка
{
    ifstream in("File.txt");
    char buff;
    in >> buff;
    for (int i = 0; i < amount; i++)
    {

        for (int j = 0; j < amount; j++)
        {
            in >> list[i][j];
            buff = in.get();
            if (buff != ' ')
            {
                strlength[i] = j + 1;
                break;
            }
        }
    }


}
bool prov(int* strlength, int** list, int amount)
{
    int* tzap = new int[amount]; // массив для элементов в одной строке

    for (int i = 0; i < amount; i++)
    {
        for (int j = 0; j < strlength[i]; j++)
        {
            if (find(tzap, tzap + j, list[i][j]) != tzap + j) // проверяем на повторение во временном массиве tzap
            {
                cout << "Введённый граф невозможен\n";
                return false;
            }

            tzap[j] = list[i][j]; //ѕрисваиваем текущий элемент текущей строки массиву tzap
        }
    }
    delete[] tzap;
    return true;
}
int main()
{
    ifstream in("File.txt");
    setlocale(LC_ALL, "Russian");
    int amount;
    in >> amount;
    int** list = new int* [amount];

    for (int i = 0; i < amount; i++)
    {
        list[i] = new int[amount];
    }

    int* strlength = new int[amount];
    vvod(strlength, list, amount); // вызов ввода

    if (!prov(strlength, list, amount)) // ѕроверка на правильность
    {
        return 0;
    }
    for (int i = 0; i < amount; i++)
    {
        bool* red = new bool[amount];
        red[i] = true;
        int current = i;
        int amount_of_visits = 0;
        int index_of_minlength = NULL;
        for (int count = 0; count < amount - 1; count++)
        {
            int minlength = 999 ;
            for (int j = 0; j < strlength[current]; j++)
            {
                if (strlength[list[current][j] - 1] < minlength && !red[list[current][j] - 1])
                {
                    index_of_minlength = j;
                    minlength = strlength[list[current][j] - 1];//
                }
            }

            if (minlength != 999)
            {
                red[list[current][index_of_minlength] - 1] = true;
                current = list[current][index_of_minlength] - 1;
                amount_of_visits++;
            }
            else
            {
                break;
            }
        }

        if (amount_of_visits != amount - 1)
        {
            cout << "граф не двусвязный\n";
            return 0;
        }
    }

    cout << "граф двусвязный\n";
}

