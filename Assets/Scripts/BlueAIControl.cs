using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class AIControl : MonoBehaviour
{

    public GameObject[] goalLocations;
    NavMeshAgent agent;
    float waitTime = 3f; // ����ͣ��ʱ��Ϊ 3 ��
    float timer = 0f;    // ��ʱ��
    bool isWaiting = false; // ��־λ�����ڱ�ʾ�Ƿ����ڵȴ�

    void Start()
    {

        agent = GetComponent<NavMeshAgent>();
        goalLocations = GameObject.FindGameObjectsWithTag("goal");
        int index = Random.Range(0, goalLocations.Length);
        agent.SetDestination(goalLocations[index].transform.position);

    }

    void Update()
    {
        // ������ڵȴ�ͣ��������¼�ʱ��
        if (isWaiting)
        {
            timer += Time.deltaTime;
            if (timer >= waitTime)
            {
                isWaiting = false;
                timer = 0f;
                SelectNextGoal();
            }
            return;
        }

        // agent ����Ŀ����ʼ�ȴ�
        if (agent.remainingDistance < 1 && !isWaiting)
        {
            isWaiting = true;
        }
    }

    void SelectNextGoal()
    {
        int index = Random.Range(0, goalLocations.Length);
        agent.SetDestination(goalLocations[index].transform.position);
    }
}