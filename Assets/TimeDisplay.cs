using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class TimeDisplay : MonoBehaviour
{
    public TMP_Text timeText;

    private const float realSecondToGameMinute = 2.0f;
    private float gameMinutes = 0.0f;
    private int days = 0;

    private void Start()
    {
        timeText = GetComponent<TMP_Text>();
    }
    private void Update()
    {
        // 获取现实时间经过的秒数
        float realSecondsPassed = Time.deltaTime;

        // 将现实时间的秒数映射为游戏内时间的分钟
        gameMinutes += realSecondsPassed * realSecondToGameMinute;

        // 将游戏内时间转换为24小时制
        int hours = Mathf.FloorToInt(gameMinutes / 60.0f + 8) % 24;
        int minutes = Mathf.FloorToInt(gameMinutes % 60.0f);
        if(gameMinutes >= 540.0f)
        {
            days++;
            gameMinutes = 0.0f;
        }

        // 更新UI Text的内容
        timeText.text = string.Format("Day {0:0}  {1:00}:{2:00}", days, hours, minutes);
    }
}