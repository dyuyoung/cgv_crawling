{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled32.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOWeDC5HNP2c4T7CyvE45Zj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dyuyoung/cgv_crawling/blob/main/Untitled.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X_6SGDb2BIRZ",
        "outputId": "6daf71f0-85e6-4bb1-c3da-f9a7ae54517c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<무비차트>----예매율 순\n",
            "1 \n",
            "\n",
            "\r\n",
            "                                2022.06.01 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "2 \n",
            "\n",
            "\r\n",
            "                                2022.05.18 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "3 \n",
            "\n",
            "\r\n",
            "                                2022.06.01 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "4 \n",
            "\n",
            "\r\n",
            "                                2022.06.08 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "D-7\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "5 \n",
            "\n",
            "\r\n",
            "                                2022.06.01 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "6 \n",
            "\n",
            "\r\n",
            "                                2022.06.01 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "7 \n",
            "\n",
            "\r\n",
            "                                2022.06.24 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "D-23\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "8 \n",
            "\n",
            "\r\n",
            "                                2022.05.04 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "9 \n",
            "\n",
            "\r\n",
            "                                2022.05.25 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "10 \n",
            "\n",
            "\r\n",
            "                                2022.05.25 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "11 \n",
            "\n",
            "\r\n",
            "                                2022.06.15 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "D-14\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "12 \n",
            "\n",
            "\r\n",
            "                                2022.06.01 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "13 \n",
            "\n",
            "\r\n",
            "                                2022.05.26 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "14 \n",
            "\n",
            "\r\n",
            "                                2022.06.02 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "D-1\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "15 \n",
            "\n",
            "\r\n",
            "                                2022.05.25 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "16 \n",
            "\n",
            "\r\n",
            "                                2022.05.18 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "17 \n",
            "\n",
            "\r\n",
            "                                2022.05.25 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "18 \n",
            "\n",
            "\r\n",
            "                                2022.05.28 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n",
            "19 \n",
            "\n",
            "\r\n",
            "                                2022.05.22 \r\n",
            "                                \n",
            "개봉\n",
            "\n",
            "\n",
            "\n",
            "\n"
          ]
        }
      ],
      "source": [
        "from urllib.request import urlopen\n",
        "from bs4 import BeautifulSoup as bs\n",
        "\n",
        "url=\"http://www.cgv.co.kr/movies/?lt=1&ft=0\"\n",
        "html=urlopen(url).read()\n",
        "\n",
        "\n",
        "soup=bs(html, \"lxml\")\n",
        "\n",
        "movies=soup.find_all(\"span\", attrs={\"class\":\"txt-info\"})\n",
        "print(\"<무비차트>----예매율 순\")\n",
        "k=[]\n",
        "for movie in movies :\n",
        "  k.append(movie.get_text('\\n'))\n",
        "for i in range(1, 20) :\n",
        "  print(i, k[i-1])"
      ]
    }
  ]
}