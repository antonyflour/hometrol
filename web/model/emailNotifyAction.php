<?php

/**
 * Created by PhpStorm.
 * User: anton
 * Date: 09/05/2017
 * Time: 18:17
 */
class EmailNotifyAction
{

    private $id;
    private $email;
    private $msg;

    /**
     * EmailNotifyAction constructor.
     * @param $id
     * @param $email
     * @param $msg
     */
    public function __construct($id, $email, $msg)
    {
        $this->id = $id;
        $this->email = $email;
        $this->msg = $msg;
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
    public function getEmail()
    {
        return $this->email;
    }

    /**
     * @param mixed $email
     */
    public function setEmail($email)
    {
        $this->email = $email;
    }

    /**
     * @return mixed
     */
    public function getMsg()
    {
        return $this->msg;
    }

    /**
     * @param mixed $msg
     */
    public function setMsg($msg)
    {
        $this->msg = $msg;
    }




}