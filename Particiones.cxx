#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

vector<double> particionar3(double total, vector<double> res, double init, int cc);
vector<double> particionar4(double total, vector<double> res, double init, int cc);

double g,m,c,t,v;

int main() {
	
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

	double lima,limb;
	cout<<"EcuaciC3n gm/c *(1-e^-((c/m)*t)) -v"<<endl;
	m=61.8;
	g=9.8;
	t=10;
	v=40;

/*	
	cout<<"Masa: ";
	cin>>m;
	cout<<"Gravedad: ";
	cin>>g;
	cout<<"Tiempo: ";
	cin>>t;
	cout<<"Velocidad: ";
	cin>>v;
*/	
	
	cout<<"Limite inferior: ";
	cin>>lima;
	cout<<"Limite superior: ";
	cin>>limb;
	
	if(lima>limb){
		cout<<"El limite inferior no puede ser mayor al superior"<<endl;
		return 0;
	}
	vector<double> res;
		
	
	double total = limb-lima;

	res = particionar3(total,res,lima, 0);

    for(int i=0;i<res.size();i++)
		cout<<(res[i]) <<endl;
	
	return 0;
}

vector<double> particionar3(double total, vector<double> res, double init,int cc){
	double zer = init, one = init+(total/3), two = init+(total*2/3), tre = init+total;
	
	zer = g*m/zer *(1-exp(-1*(zer/m)*t))-v;
	one = g*m/one *(1-exp(-1*(one/m)*t))-v;
	two = g*m/two *(1-exp(-1*(two/m)*t))-v;
	tre = g*m/tre *(1-exp(-1*(tre/m)*t))-v;
	
	cout<<"Interaccion #"<<cc<<endl;
	
	if(zer == 0){
		res.push_back(init);
		return res;
	}
	if(one == 0){
		res.push_back(init+(total/3));
		return res;
	}
	if(two == 0){
		res.push_back(init+(total*2/3));
		return res;
	}
	if(tre == 0){
		res.push_back(init+total);
		return res;
	}
	
	total = total/3;
	if(cc<=10){
		if(zer*one<0){
		    res = particionar3(total,res, init,cc+1);
		}if(one*two<0){
			res = particionar3(total,res, init+total,cc+1);
		}if(two*tre<0){
			res = particionar3(total,res, init+total*2,cc+1);
		}
	}
	else{
		if(zer*one<0){
			res.push_back((init+init+total)/2);
		}if(one*two<0){
			res.push_back((init+total+init+total*2)/2);
		}if(two*tre<0){
			res.push_back((init+total*2+init+total*3)/2);
		}
	}
	return res;
}

vector<double> particionar4(double total, vector<double> res, double init,int cc){
	double zer = init, one = init+(total/4), two = init+(total*2/4), tre = init+(total*3/4), fou = init+total;
	
	zer = g*m/zer *(1-exp(-1*(zer/m)*t))-v;
	one = g*m/one *(1-exp(-1*(one/m)*t))-v;
	two = g*m/two *(1-exp(-1*(two/m)*t))-v;
	tre = g*m/tre *(1-exp(-1*(tre/m)*t))-v;
	fou = g*m/tre *(1-exp(-1*(fou/m)*t))-v;
	
	
	if(zer == 0){
		res.push_back(init);
		return res;
	}
	if(one == 0){
		res.push_back(init+(total/4));
		return res;
	}
	if(two == 0){
		res.push_back(init+(total*2/4));
		return res;
	}
	if(tre == 0){
		res.push_back(init+(total*3/4));
		return res;
	}
	if(fou == 0){
		res.push_back(init+total);
		return res;
	}
	
	total = total/4;
	if(cc<=20){
		if(zer*one<0){
		    res = particionar3(total,res, init,cc+1);
		}if(one*two<0){
			res = particionar3(total,res, init+total,cc+1);
		}if(two*tre<0){
			res = particionar3(total,res, init+total*2,cc+1);
		}if(tre*fou<0){
			res = particionar4(total,res, init+total*3,cc+1);
		}
	}
	else{
		if(zer*one<0){
			res.push_back((init+init+total)/2);
		}if(one*two<0){
			res.push_back((init+total+init+total*2)/2);
		}if(two*tre<0){
			res.push_back((init+total*2+init+total*3)/2);
		}if(tre*fou<0){
			res.push_back((init+total*3+init+total*4)/2);
		}
	}
	
	return res;
}
