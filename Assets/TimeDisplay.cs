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
        // ��ȡ��ʵʱ�侭��������
        float realSecondsPassed = Time.deltaTime;

        // ����ʵʱ�������ӳ��Ϊ��Ϸ��ʱ��ķ���
        gameMinutes += realSecondsPassed * realSecondToGameMinute;

        // ����Ϸ��ʱ��ת��Ϊ24Сʱ��
        int hours = Mathf.FloorToInt(gameMinutes / 60.0f + 8) % 24;
        int minutes = Mathf.FloorToInt(gameMinutes % 60.0f);
        if(gameMinutes >= 540.0f)
        {
            days++;
            gameMinutes = 0.0f;
        }

        // ����UI Text������
        timeText.text = string.Format("Day {0:0}  {1:00}:{2:00}", days, hours, minutes);
    }
}