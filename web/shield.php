<?php

/**
 * Created by PhpStorm.
 * User: anton
 * Date: 02/05/2017
 * Time: 20:39
 */
class Shield{

    private $mac;
    private $nome;
    private $ip;
    private $port;
    private $input_pin; //array
    private $output_pin; //array

    /**
     * Shield constructor.
     * @param $mac
     * @param $nome
     * @param $ip
     * @param $port
     * @param $input_pin
     * @param $output_pin
     */
    public function __construct($mac, $nome, $ip, $port, $input_pin, $output_pin)
    {
        $this->mac = $mac;
        $this->nome = $nome;
        $this->ip = $ip;
        $this->port = $port;
        $this->input_pin = $input_pin;
        $this->output_pin = $output_pin;
    }

    /**
     * @return mixed
     */
    public function getMac()
    {
        return $this->mac;
    }

    /**
     * @param mixed $mac
     */
    public function setMac($mac)
    {
        $this->mac = $mac;
    }

    /**
     * @return mixed
     */
    public function getNome()
    {
        return $this->nome;
    }

    /**
     * @param mixed $nome
     */
    public function setNome($nome)
    {
        $this->nome = $nome;
    }

    /**
     * @return mixed
     */
    public function getIp()
    {
        return $this->ip;
    }

    /**
     * @param mixed $ip
     */
    public function setIp($ip)
    {
        $this->ip = $ip;
    }

    /**
     * @return mixed
     */
    public function getPort()
    {
        return $this->port;
    }

    /**
     * @param mixed $port
     */
    public function setPort($port)
    {
        $this->port = $port;
    }

    /**
     * @return mixed
     */
    public function getInputPin()
    {
        return $this->input_pin;
    }

    /**
     * @param mixed $input_pin
     */
    public function setInputPin($input_pin)
    {
        $this->input_pin = $input_pin;
    }

    /**
     * @return mixed
     */
    public function getOutputPin()
    {
        return $this->output_pin;
    }

    /**
     * @param mixed $output_pin
     */
    public function setOutputPin($output_pin)
    {
        $this->output_pin = $output_pin;
    }




}