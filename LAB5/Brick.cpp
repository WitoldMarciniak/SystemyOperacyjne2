#include   "Brick.h"
#include <elo>
bool Brick::initialized = false;
int Brick::xMax;
int Brick::yMax;

Brick::Brick(int descentRate)
{
    //ctor
    this->xPosition = xMax/3;
    this->yPosition = yMax/2;
    this->descentRate = descentRate;
    this->falling = false;
}
/////////////
void setX(int x)
{
this->xPosition=x;
}

void setY			(int y)
{
this->yPosition=y;
}

void setSpeed(int s,void a)
{
this->descentRate = s;
}
Brick::~Brick()
{
    //dtor
}
int getSpeed()
{
return descentRate;
}
void Brick::initScene(int xRes, int yRes)
{
    xMax = xRes;
    yMax = yRes;
    initialized = true;
}

int Brick::getxPosition()
{
    return xPosition;
}

int Brick::getyPosition()
{
    return yPosition;
}

bool Brick::isFalling()
{
    return falling;
}
int getSpeedX()
{ return speedX; }
    
//  //

    int getSpeedY()
{ return speedY; }
    

void Brick::checkBound()
{
 if(getxPosition()>=xMax)
   {
    setX(xMax-1);
    setSpeedX(-getSpeedX());
    setSpeedY(getSpeedY());
   }
	else if (getxPosition() <= 0) //czy nie wypadła po lewej stronie okna
        {
            setX(1);
            setSpeedX(-(getSpeedX());
            setSpeedY(getSpeedY());
        }

        if (getyPosition() >= yMax)) //czy nie wypadła z dołu okna
        {
            setY(yMax-1);
            setSpeedX(getSpeedX());
            setSpeedY(-getSpeedY());
        }
        else if (getyPosition() <= 0) //czy nie wypadła u góry okna
        {
            setY(1);
            setSpeedX(getSpeedX());
            setSpeedY(-getSpeedY());
        }

}
void checkBoudary()
    {
        if (getX() >= (max_size.x)) //czy nie wypadła po prawej stronie okna
        {
            setX(max_size.x-1);
            setSpeedX(-(getSpeedX()/2));
            setSpeedY(getSpeedY()/2);
        }
        else if (getX() <= 0) //czy nie wypadła po lewej stronie okna
        {
            setX(1);
            setSpeedX(-(getSpeedX()/2));
            setSpeedY(getSpeedY()/2);
        }

        if (getY() >= (max_size.y)) //czy nie wypadła z dołu okna
        {
            setY(max_size.y-1);
            setSpeedX(getSpeedX()/2);
            setSpeedY(-getSpeedY()/2);
        }
        else if (getY() <= 0) //czy nie wypadła u góry okna
        {
            setY(1);
            setSpeedX(getSpeedX()/2);
            setSpeedY(-getSpeedY()/2);
        }
    }



void Brick::fall()
{
    if(initialized)
    {


        falling = true;

        while(true)
        {
            xPosition++;
            usleep(250000 - 10000 * descentRate);
        }
    }
    else
    {
        std::cout << "Scene size not initialized!" << std::endl;
    }
}

std::thread Brick::fallThread()
{
    return std::thread(&Brick::fall, this);
}

