#include <stdio.h>
#include <gsl/gsl_integration.h>

double my_cquad ( double my_f() , double a , double b  )
{
    gsl_function f;
    gsl_integration_cquad_workspace *ws = NULL;
    double res, abserr;
    size_t neval;

    /* Prepare the function. */
    f.function = my_f;
    f.params = NULL;

    /* Initialize the workspace. */
    if ( ( ws = gsl_integration_cquad_workspace_alloc( 200 ) ) == NULL ) {
        printf( "call to gsl_integration_cquad_workspace_alloc failed.\n" );
        abort();
        }

    /* Call the integrator. */
    if ( gsl_integration_cquad( &f, a , b , 1.0e-10 , 1.0e-10 , ws , &res , &abserr , &neval ) != 0 ) {
        printf( "call to gsl_integration_cquad failed.\n" );
        abort();
        }

    /* Free the workspace. */
    gsl_integration_cquad_workspace_free( ws );

    /* Bye. */
    return res;
}