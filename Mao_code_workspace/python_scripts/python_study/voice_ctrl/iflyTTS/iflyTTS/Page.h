#ifndef _PAGE
#define _PAGE
#include <string>
#include <list>
using namespace std;


class Element
{
public:
	bool m_isEnglish;
	string m_content;
};


class Sentence
{
public:
	list<Element>  m_sentence;
};

#endif