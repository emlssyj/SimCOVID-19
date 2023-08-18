using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;

public class AIControl : MonoBehaviour
{

    public GameObject[] goalLocations;
    NavMeshAgent agent;
    float waitTime = 3f; // 设置停留时间为 3 秒
    float timer = 0f;    // 计时器
    bool isWaiting = false; // 标志位，用于表示是否正在等待

    void Start()
    {

        agent = GetComponent<NavMeshAgent>();
        goalLocations = GameObject.FindGameObjectsWithTag("goal");
        int index = Random.Range(0, goalLocations.Length);
        agent.SetDestination(goalLocations[index].transform.position);

    }

    void Update()
    {
        // 如果正在等待停留，则更新计时器
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

        // agent 到达目标点后开始等待
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