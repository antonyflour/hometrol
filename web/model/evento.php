<?php

/**
 * Created by PhpStorm.
 * User: anton
 * Date: 06/05/2017
 * Time: 18:43
 */
class Evento
{

    private $id;
    private $enabled;
    private $lastExecTime;
    private $repetitionInterval;
    private $condition;
    private $action;

    /**
     * Evento constructor.
     * @param $id
     * @param $enabled
     * @param $lastExecTime
     * @param $repetitionInterval
     * @param $condition
     * @param $action
     */
    public function __construct($id, $enabled, $lastExecTime, $repetitionInterval, $condition, $action)
    {
        $this->id = $id;
        $this->enabled = $enabled;
        $this->lastExecTime = $lastExecTime;
        $this->repetitionInterval = $repetitionInterval;
        $this->condition = $condition;
        $this->action = $action;
    }

    /**
     * @return mixed
     */
    public function getId()
    {
        return $this->id;
    }

    /**
     * @param mixed $id
     */
    public function setId($id)
    {
        $this->id = $id;
    }

    /**
     * @return mixed
     */
    public function getEnabled()
    {
        return $this->enabled;
    }

    /**
     * @param mixed $enabled
     */
    public function setEnabled($enabled)
    {
        $this->enabled = $enabled;
    }

    /**
     * @return mixed
     */
    public function getLastExecTime()
    {
        return $this->lastExecTime;
    }

    /**
     * @param mixed $lastExecTime
     */
    public function setLastExecTime($lastExecTime)
    {
        $this->lastExecTime = $lastExecTime;
    }

    /**
     * @return mixed
     */
    public function getRepetitionInterval()
    {
        return $this->repetitionInterval;
    }

    /**
     * @param mixed $repetitionInterval
     */
    public function setRepetitionInterval($repetitionInterval)
    {
        $this->repetitionInterval = $repetitionInterval;
    }

    /**
     * @return mixed
     */
    public function getCondition()
    {
        return $this->condition;
    }

    /**
     * @param mixed $condition
     */
    public function setCondition($condition)
    {
        $this->condition = $condition;
    }

    /**
     * @return mixed
     */
    public function getAction()
    {
        return $this->action;
    }

    /**
     * @param mixed $action
     */
    public function setAction($action)
    {
        $this->action = $action;
    }




}