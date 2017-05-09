<?php

/**
 * Created by PhpStorm.
 * User: anton
 * Date: 06/05/2017
 * Time: 18:45
 */
class PinStateAlterationCondition
{

    private $id;
    private $shield;
    private $pin;
    private $expected_state;

    /**
     * PinStateAlterationCondition constructor.
     * @param $id
     * @param $shield
     * @param $pin
     * @param $expected_state
     */
    public function __construct($id, $shield, $pin, $expected_state)
    {
        $this->id = $id;
        $this->shield = $shield;
        $this->pin = $pin;
        $this->expected_state = $expected_state;
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
    public function getShield()
    {
        return $this->shield;
    }

    /**
     * @param mixed $shield
     */
    public function setShield($shield)
    {
        $this->shield = $shield;
    }

    /**
     * @return mixed
     */
    public function getPin()
    {
        return $this->pin;
    }

    /**
     * @param mixed $pin
     */
    public function setPin($pin)
    {
        $this->pin = $pin;
    }

    /**
     * @return mixed
     */
    public function getExpectedState()
    {
        return $this->expected_state;
    }

    /**
     * @param mixed $expected_state
     */
    public function setExpectedState($expected_state)
    {
        $this->expected_state = $expected_state;
    }




}